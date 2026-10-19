"""Reproduce completed R1 model results. All inputs are synthetic and declared here."""
from pathlib import Path
import json,csv,sys,platform
import numpy as np
import scipy
from scipy.optimize import minimize,brentq
import sympy as sp
from admission_model import allocation,solve_qp,serial
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'results_R1';OUT.mkdir(exist_ok=True)

def save(name,obj):
    (OUT/name).write_text(json.dumps(obj,indent=2,default=lambda x:float(x))+'\n')
def writecsv(name,rows):
    with (OUT/name).open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
# Example 1: nonrival provision and documentation, low-value opening.
p=dict(V=[[.5,.1],[.1,.4]],K=np.diag([4.,5.]),n=[1,1],a=[1,1],gamma=.5,C=20,kappa=1)
opening=[]
for h2 in [-1,.5]:
    for mode in ['unpriced','support_priced','full_information']:
        beta=1 if mode=='full_information' else .5
        s=allocation(h=[4,h2],**p,beta=beta,tolled=mode!='unpriced',upper=[10,10] if mode=='unpriced' else None)
        opening.append(dict(h2=h2,policy=mode,q=s['z'][0],d=s['z'][1],y1=s['y'][0],y2=s['y'][1],load=s['A'],welfare=s['W']))
assert opening[3]['welfare']<opening[0]['welfare']
assert abs(opening[4]['welfare']-opening[1]['welfare'])<1e-10
writecsv('opening.csv',opening)
# Example 2: private producer cost, common fee, zero central reserve.
p2=dict(h=[2,1],V=[[1,.2],[.2,.8]],K=np.diag([2,2]),n=[1,1],a=[1,1],gamma=.15,C=10)
types=[1,2]
def stats(beta):return [allocation(**p2,kappa=k,beta=beta) for k in types]
def reserve(beta):
    ss=stats(beta);return max(s['T']-s['Gamma'] for s in ss)-min(s['R'] for s in ss)
bstar=brentq(reserve,.4,.7,xtol=1e-14);ss=stats(bstar);fee=min(s['R'] for s in ss)
rows=[]
for k in types:
    for label,beta,priced in [('decentralized',.2,False),('support_only',0,True),('implementable',bstar,True),('full_information',1,True)]:
        s=allocation(**p2,kappa=k,beta=beta,tolled=priced,upper=[5,5] if not priced else None)
        rows.append(dict(kappa=k,policy=label,beta=beta,q=s['z'][0],d=s['z'][1],y1=s['y'][0],y2=s['y'][1],welfare=s['W'],transfer=s['T'],producer_cost=s['production_cost'],rent=s['R'],support_surplus=s['Gamma'],fee=fee if label=='implementable' else '',central_deficit=s['T']-s['Gamma']-fee if label=='implementable' else ''))
        if label=='implementable':assert s['R']>=fee-1e-10 and s['T']-s['Gamma']-fee<=1e-10
full=stats(1);Bprivate=max(0,reserve(1));Bknown=max(0,max(s['production_cost']-s['Gamma'] for s in full))
assert Bprivate>Bknown>0
writecsv('private_cost.csv',rows)
# Exact symbolic isolation of ALL financing boundaries for Example 2.
b=sp.symbols('b',real=True);V=sp.Matrix([[1,sp.Rational(1,5)],[sp.Rational(1,5),sp.Rational(4,5)]]);K=2*sp.eye(2);h=sp.Matrix([2,1]);a=sp.ones(2,1);H=sp.eye(2)+sp.Rational(3,20)*a*a.T;Q=V*K.inv()*V.T
y0=H.inv()*h;G0=(h.T*y0-(y0.T*H*y0)/2)[0]
exact=[]
for k in types:
    y=(H-b*Q/k).inv()*h;z=b/k*K.inv()*V.T*y
    G=(h.T*y+z.T*V.T*y-y.T*H*y/2)[0];C=(k*z.T*K*z/2)[0]
    T=sp.factor(b*(G-G0));R=sp.factor(T-C);Gam=sp.factor(sp.Rational(3,40)*(a.T*y)[0]**2)
    # Certify that the example stays on its declared active branch.
    for guard in [*list(y),sp.Integer(10)-(a.T*y)[0]]:
        gn,gd=sp.fraction(sp.factor(guard))
        assert float(guard.subs(b,sp.Rational(1,2)))>0
        assert not any(float((lo+hi)/2)>0 and float((lo+hi)/2)<1 for (lo,hi),_ in sp.Poly(gn,b).intervals(eps=sp.Rational(1,10**12)))
    exact.append((T,R,Gam))
roots=[];constraints=[]
for i in range(2):
    for j in range(2):
        expr=sp.factor(exact[i][0]-exact[i][2]-exact[j][1]);num,den=sp.fraction(expr)
        ints=sp.Poly(num,b).intervals(eps=sp.Rational(1,10**12))
        rr=[]
        for (lo,hi),multiplicity in ints:
            midpoint=float((lo+hi)/2)
            if 0<midpoint<1:
                rr.append(midpoint);roots.append(midpoint)
        constraints.append(dict(paying_type=types[i],participation_type=types[j],numerator=str(num),denominator=str(den),roots_in_0_1=rr))
points=sorted(set([0.,1.]+roots));intervals=[]
for lo,hi in zip(points[:-1],points[1:]):
    mid=(lo+hi)/2
    feasible=all(float((ti-gi-rj).subs(b,mid))<=1e-9 for ti,_,gi in exact for _,rj,_ in exact)
    intervals.append(dict(lower=lo,upper=hi,feasible=feasible))
feasible_upper=max(x['upper'] for x in intervals if x['feasible']);assert abs(feasible_upper-bstar)<1e-10
save('financing_certificate.json',dict(beta_star=bstar,fee=fee,B_private_at_full=Bprivate,B_known_at_full=Bknown,constraints=constraints,intervals=intervals,assumptions='Example 2 has all uses positive and slack capacity over beta in [0,1]; denominators nonzero by positive definiteness. Roots isolated with exact rational polynomial coefficients.'))
# Example 3: endogenous-use, two-margin mixed-sign factorial, exact rationals.
Vm=sp.Matrix([[1,sp.Rational(1,10)],[sp.Rational(1,10),1]]);Km=2*sp.eye(2);am=sp.Matrix([1,2]);Hm=sp.eye(2)+sp.Rational(1,10)*am*am.T;Qm=Vm*Km.inv()*Vm.T
cells={};mixedrows=[]
for t in [0,1]:
    hm=sp.Matrix([4,1+t])
    for beta in [sp.Rational(2,5),sp.Rational(7,10)]:
        y=(Hm-beta*Qm).inv()*hm;z=beta*Km.inv()*Vm.T*y
        W=(hm.T*y+z.T*Vm.T*y-y.T*Hm*y/2-z.T*Km*z/2)[0]
        assert min(y)>0 and (am.T*y)[0]<100
        cells[t,beta]=(z[0],z[1],W)
        mixedrows.append(dict(T=t,beta=float(beta),q=float(z[0]),d=float(z[1]),welfare=float(W)))
def cross(pos):return sp.factor(cells[1,sp.Rational(7,10)][pos]-cells[1,sp.Rational(2,5)][pos]-cells[0,sp.Rational(7,10)][pos]+cells[0,sp.Rational(2,5)][pos])
qcross,dcross,wcross=[cross(i) for i in range(3)];assert qcross<0 and dcross>0 and wcross>0
writecsv('endogenous_interaction.csv',mixedrows)
save('exact_interaction.json',dict(quantity=str(qcross),documentation=str(dcross),welfare=str(wcross),quantity_decimal=float(qcross),documentation_decimal=float(dcross),welfare_decimal=float(wcross)))
# Independent original-dimensional constrained optimizations, including active boundaries.
cases=[]
base=dict(h=[2,1],V=[[1,.2],[.2,.8]],K=np.diag([2,2]),n=[1,1],a=[1,1],gamma=.15,C=10)
for hh,cap,beta,k in [([2,1],10,.5,1),([2,1],2,1,1),([2,1],2,1,2),([-2,-1],2,1,1),([2,-3],1,.7,1),([0,0],3,0,2),([2,1],10,1,2),([2,1],.01,.4,1)]:
    pp={**base,'h':hh,'C':cap};s=allocation(**pp,beta=beta,kappa=k)
    VV=np.array(pp['V']);KK=pp['K'];aa=np.array(pp['a']);HH=np.diag(1/np.array(pp['n']))+pp['gamma']*np.outer(aa,aa);hv=np.array(hh)
    if beta:
        def objective(x):
            z=x[:2];y=x[2:];return -beta*(hv@y+z@VV.T@y-.5*y@HH@y)+.5*k*z@KK@z
        fit=minimize(objective,np.zeros(4),method='SLSQP',bounds=[(0,None)]*4,constraints=[{'type':'ineq','fun':lambda x:cap-aa@x[2:]}],options={'ftol':1e-12,'maxiter':1000})
        error=abs(fit.fun-objective(np.r_[s['z'],s['y']]));assert fit.success and error<1e-8,(fit.message,error)
    else:error=0
    cases.append(dict(h=hh,capacity=cap,beta=beta,kappa=k,nu=s['nu'],y=s['y'].tolist(),objective_error=error))
# Explicit sequential gross-credit trap: all consumer classes remain interior.
Vg=np.array([[1,.2],[.2,.8]]);Kg=np.diag([4.,4.]);hg=np.array([2.,1.]);ag=np.ones(2);Hg=np.eye(2)+.15*np.outer(ag,ag);J=Vg.T@np.linalg.solve(Hg,Vg);bg=Vg.T@np.linalg.solve(Hg,hg)
assert np.linalg.eigvalsh(Kg-2*J).min()>0
zgross=np.linalg.solve(Kg-2*J,bg);zcorrect=np.linalg.solve(Kg-J,bg)
def wg(z):
    y=np.linalg.solve(Hg,hg+Vg@z);return hg@y+z@Vg.T@y-.5*y@Hg@y-.5*z@Kg@z
assert wg(zgross)<wg(zcorrect)
save('verification_R1.json',dict(synthetic_only=True,independent_optimization_cases=cases,max_objective_error=max(x['objective_error'] for x in cases),gross_credit=dict(correct_z=zcorrect.tolist(),gross_z=zgross.tolist(),correct_W=wg(zcorrect),gross_W=wg(zgross)),exact_checks=['rational mixed-sign contrasts','all financing boundaries isolated','IR and center budget at beta_star'],python=sys.version,numpy=np.__version__,scipy=scipy.__version__,sympy=sp.__version__))
# Scientific figures, generated directly from the solved model, not empirical data.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
bs=np.linspace(0,1,201);required=[];w1=[];w2=[]
for bb in bs:
    zz=stats(bb);required.append(max(0,max(r['T']-r['Gamma'] for r in zz)-min(r['R'] for r in zz)));w1.append(zz[0]['W']);w2.append(zz[1]['W'])
fig,ax=plt.subplots(1,2,figsize=(9.2,3.4))
ax[0].plot(bs,required,color='#25485e');ax[0].axvline(bstar,color='#a54f2f',linestyle='--');ax[0].set(xlabel='Verified-surplus credit share beta',ylabel='Minimum central reserve',title='A. Financing and participation')
ax[1].plot(bs,w1,label='Cost type 1',color='#25485e');ax[1].plot(bs,w2,label='Cost type 2',color='#5a8864');ax[1].axvline(bstar,color='#a54f2f',linestyle='--',label='Zero-reserve optimum');ax[1].set(xlabel='Verified-surplus credit share beta',ylabel='Organizational surplus',title='B. Constrained provision');ax[1].legend(frameon=False,fontsize=8)
for aa in ax:aa.spines[['top','right']].set_visible(False)
fig.tight_layout();fig.savefig(OUT/'financing.png',dpi=200);plt.close(fig)
print(json.dumps({'beta_star':bstar,'fee':fee,'B_private_at_full':Bprivate,'B_known_at_full':Bknown,'quantity_interaction':float(qcross),'documentation_interaction':float(dcross),'welfare_interaction':float(wcross),'max_independent_objective_error':max(x['objective_error'] for x in cases)},indent=2))
