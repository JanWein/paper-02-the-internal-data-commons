"""Run preserved R1 results and one exact crossing-baseline score regression.

All inputs are synthetic. No network, observed data, or random simulation.
Run from the package root: python3 code/reproduce_R2.py
"""
from pathlib import Path
import hashlib
import itertools
import json
import subprocess
import sys
import numpy as np
import sympy as s
from admission_model import allocation

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results_R2'
OUT.mkdir(exist_ok=True)
names = ['opening.csv', 'private_cost.csv', 'financing_certificate.json',
         'endogenous_interaction.csv', 'exact_interaction.json']
before = {n: hashlib.sha256((ROOT/'history/central_R1_complete/results_R1'/n).read_bytes()).hexdigest() for n in names}
subprocess.run([sys.executable, str(ROOT/'code/reproduce_R1.py')], cwd=ROOT, check=True)
after = {n: hashlib.sha256((ROOT/'results_R1'/n).read_bytes()).hexdigest() for n in names}
assert before == after, 'A preserved R1 numerical result changed'

R = s.Rational
D = s.eye(2)
a = s.ones(2, 1)
K = 2*s.eye(2)
V = s.Matrix([[1, R(1,5)], [R(1,5), R(4,5)]])
h = s.Matrix([4, -R(1,10)])
gamma = R(3,20)
capacity = s.Integer(10)
H = D + gamma*a*a.T
Q = V*K.inv()*V.T

def scalar(x):
    return s.factor(x[0])

def exact_qp(M):
    """Enumerate all support sets and both capacity states in rational arithmetic."""
    candidates = []
    for flags in itertools.product([False, True], repeat=2):
        S = [i for i in range(2) if flags[i]]
        for binding in [False, True]:
            if binding and not S:
                continue
            y = s.zeros(2,1)
            nu = s.Integer(0)
            if S:
                MS = M.extract(S,S)
                hs, aa = h.extract(S,[0]), a.extract(S,[0])
                if binding:
                    nu = s.factor((scalar(aa.T*MS.inv()*hs)-capacity)/scalar(aa.T*MS.inv()*aa))
                ys = MS.inv()*(hs-nu*aa)
                for i,v in zip(S,ys): y[i] = s.factor(v)
            gradient = h-M*y-nu*a
            if nu < 0 or any(v < 0 for v in y) or scalar(a.T*y)>capacity:
                continue
            if binding and scalar(a.T*y)!=capacity:
                continue
            if any(gradient[i]!=0 if flags[i] else gradient[i]>0 for i in range(2)):
                continue
            value = scalar(h.T*y-y.T*M*y/2)
            candidates.append((value,y,nu))
    assert candidates
    return max(candidates, key=lambda x:x[0])

# Independent derivation from the constrained programs, not supplied fractions.
assert (D-Q)[0,0]>0 and (D-Q).det()>0
G0,y0,nu0 = exact_qp(H)
_,y,nu = exact_qp(H-Q)
z = K.inv()*V.T*y
G = scalar((h+V*z).T*y-y.T*H*y/2)
T = s.factor(G-G0)
cost = scalar(z.T*K*z/2)
rent = s.factor(T-cost)
load = scalar(a.T*y)
support = s.factor(gamma*load**2/2)
revenue = s.factor(gamma*load**2)
Gamma = s.factor(revenue-support)
unconstrained_G0 = scalar(h.T*H.inv()*h/2)
c0 = s.factor(unconstrained_G0-G0)
b, J = V.T*H.inv()*h, V.T*H.inv()*V
polynomial = scalar(b.T*z+z.T*J*z/2)
wrong_rent = s.factor(polynomial-cost)
assert G0 == R(160,23) and y0 == s.Matrix([R(80,23),0])
assert y == s.Matrix([R(5395,849),R(95,849)])
assert z == s.Matrix([R(2707,849),R(385,566)])
assert polynomial-T == -R(1573,9200)
assert T == polynomial+c0 and nu==nu0==0 and all(v>0 for v in y)
assert load<capacity and (h-H*y0)[1]<0
assert (H*y-h-V*z)==s.zeros(2,1)
assert K*z == V.T*y

# Settlement at F=0 and then at each score's maximal weak-IR fee.
fixed_fee_deficit = s.factor(T-Gamma)
wrong_fixed_fee_deficit = s.factor(polynomial-Gamma)
max_fee_deficit = s.factor(T-Gamma-rent)
wrong_max_fee_deficit = s.factor(polynomial-Gamma-wrong_rent)
assert fixed_fee_deficit-wrong_fixed_fee_deficit == c0
assert rent-wrong_rent == c0
assert max_fee_deficit == wrong_max_fee_deficit == cost-Gamma
float_case = allocation(h=np.array(h,float).ravel(), V=np.array(V,float),
    K=np.array(K,float), n=[1,1], a=[1,1], gamma=float(gamma),
    C=10, kappa=1, beta=1)
for name, exact in [('T',T),('R',rent),('G0',G0),('G',G),('Gamma',Gamma)]:
    assert abs(float_case[name]-float(exact))<1e-10
assert np.max(np.abs(float_case['z']-np.array(z,float).ravel()))<1e-10

def enc(x):
    if isinstance(x,s.MatrixBase): return [str(v) for v in x]
    return str(x)

values = dict(y0=y0,G0=G0,unconstrained_y0=H.inv()*h,
    unconstrained_G0=unconstrained_G0,y=y,z=z,load=load,G=G,
    branch_constant=c0,branch_polynomial=polynomial,actual_score=T,
    production_cost=cost,wrong_rent=wrong_rent,actual_rent=rent,
    support_cost=support,support_revenue=revenue,Gamma=Gamma,
    wrong_fixed_fee_deficit=wrong_fixed_fee_deficit,
    actual_fixed_fee_deficit=fixed_fee_deficit,
    fixed_fee_required_reserve=max(s.Integer(0),fixed_fee_deficit),
    wrong_max_weak_IR_fee=wrong_rent,actual_max_weak_IR_fee=rent,
    max_fee_required_reserve=max(s.Integer(0),max_fee_deficit),
    wrong_max_fee_required_reserve=max(s.Integer(0),wrong_max_fee_deficit))
report = dict(synthetic_only=True,exact={k:enc(v) for k,v in values.items()},
    decimals={k:float(v) for k,v in values.items() if not isinstance(v,s.MatrixBase)},
    checks=dict(all_supplied_fractions_independently_derived=True,
        baseline_KKT=True,optimal_KKT=True,assumption_A=True,
        score_matches_active_set_implementation=True,
        old_R1_numerical_files_byte_identical=before==after),
    preserved_R1_sha256=after)
(OUT/'crossing_baseline_exact.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
