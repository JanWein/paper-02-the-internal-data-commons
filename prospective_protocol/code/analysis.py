"""Synthetic model verification; no observations from firms. Python 3 standard library."""
from pathlib import Path
import csv, itertools, json, math, random
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results'; OUT.mkdir(exist_ok=True)
def state(B,D,H,a):
    q=max(a*B-D,0)/H
    return q,(B-D)*q-H*q*q/2
rows=[]
for name,h1 in [('complements',4.4),('quantity_substitute_welfare_complement',5.2),('substitutes',7.0)]:
    cells={}
    for t,a in itertools.product([0,1],[.4,.7]):
        B,D,H=(10.,1.,4.) if t==0 else (12.,1.2,h1)
        q,w=state(B,D,H,a);cells[t,a]=(q,w)
        rows.append(dict(scenario=name,T=t,alpha=a,B=B,D=D,H=H,q=q,welfare=w))
    dq=cells[1,.7][0]-cells[1,.4][0]-cells[0,.7][0]+cells[0,.4][0]
    dw=cells[1,.7][1]-cells[1,.4][1]-cells[0,.7][1]+cells[0,.4][1]
    rows.append(dict(scenario=name,T='interaction',alpha='',B='',D='',H='',q=dq,welfare=dw))
with (OUT/'factorial.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
rng=random.Random(20261017);checks=0;max_err=0
for _ in range(10000):
    B=rng.uniform(.1,30);D=rng.uniform(0,5);H=rng.uniform(.2,20);a=rng.uniform(0,1)
    q,w=state(B,D,H,a);qs,ws=state(B,D,H,1)
    assert q<=qs+1e-12 and w<=ws+1e-10
    # Exact loss identity includes corner regimes through the clipped q's.
    loss=H*(qs-q)**2/2 if B>D else 0
    assert abs(ws-w-loss)<1e-9
    if a*B>D+.01 and a<.99:
        eps=1e-5
        fd=(state(B,D,H,a+eps)[1]-state(B,D,H,a-eps)[1])/(2*eps)
        exact=(1-a)*B*B/H;max_err=max(max_err,abs(fd-exact))
        assert abs(fd-exact)<1e-6
    checks+=1
# Exact randomization enumeration, independent assignment of 6 clusters to 4 arms.
# Each outcome has two upstream neighbors. Exposure is any neighbor in arm 11.
N=6
sums={(z,e):0. for z in [0,3] for e in [0,1]}
means={(z,e):sum((i/10)+(.65 if z==3 else 0)+.25*e for i in range(N))/N for z,e in sums}
for zz in itertools.product(range(4),repeat=N):
    for z,e in sums:
        ht=0
        for i in range(N):
            ee=int(zz[(i-1)%N]==3 or zz[(i-2)%N]==3)
            if zz[i]==z and ee==e:
                T=zz[i]//2;I=zz[i]%2
                y=i/10+.3*T+.2*I+.15*T*I+.25*ee
                pi=.25*((9/16) if e==0 else (7/16))
                ht+=y/pi/N
        sums[z,e]+=ht/(4**N)
assert all(abs(sums[k]-means[k])<1e-11 for k in sums)
# Planning precision: balanced 4-arm cluster randomization, standardized cluster SD=1.
# Main factorial averaged effect SE=2/sqrt(K); interaction SE=4/sqrt(K).
power=[]
for K in [40,80,160,320]:
    power.append(dict(clusters=K,clusters_per_cell=K//4,main_MDE=2.802*2/math.sqrt(K),interaction_MDE=2.802*4/math.sqrt(K),holm3_main_MDE=3.236*2/math.sqrt(K),holm3_interaction_MDE=3.236*4/math.sqrt(K)))
with (OUT/'precision.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=power[0]);w.writeheader();w.writerows(power)
report={'synthetic_only':True,'seed':20261017,'random_parameter_checks':checks,'max_welfare_derivative_absolute_error':max_err,'exact_assignments':4**N,'exposure_means':[{ 'own_arm':z,'exposure':e,'HT_expectation':sums[z,e],'truth':means[z,e]} for z,e in sums]}
(OUT/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2));print('Factorial results:');print((OUT/'factorial.csv').read_text());print((OUT/'precision.csv').read_text())
# General convex costs: C=H0 exp(h*t) q^2/2 + eta*q^3/3.
def general(t,a,B0,D0,H0,b,d,h,eta):
    B=B0*math.exp(b*t);D=D0*math.exp(d*t);H=H0*math.exp(h*t)
    n=a*B-D
    q=2*n/(H+math.sqrt(H*H+4*eta*n))
    w=(B-D)*q-H*q*q/2-eta*q**3/3
    return q,w,B,D,H
max_qerr=max_werr=0.
for _ in range(1000):
    B0=rng.uniform(5,20);D0=rng.uniform(.1,1);H0=rng.uniform(2,8)
    b,d,h=[rng.uniform(-.2,.4) for _ in range(3)];eta=rng.uniform(.1,2);a=rng.uniform(.3,.8);t=.2
    args=(B0,D0,H0,b,d,h,eta)
    q,w,B,D,H=general(t,a,*args);K=H+2*eta*q
    qt=(a*b*B-d*D-h*H*q)/K
    Kt=h*H+2*eta*qt
    qa_t=(b*B*K-B*Kt)/(K*K)
    wa_t=(1-a)*(2*b*B*B*K-B*B*Kt)/(K*K)
    eps=.0001
    vals=[general(t+st*eps,a+sa*eps,*args) for st,sa in [(1,1),(1,-1),(-1,1),(-1,-1)]]
    fdq=(vals[0][0]-vals[1][0]-vals[2][0]+vals[3][0])/(4*eps*eps)
    fdw=(vals[0][1]-vals[1][1]-vals[2][1]+vals[3][1])/(4*eps*eps)
    max_qerr=max(max_qerr,abs(fdq-qa_t));max_werr=max(max_werr,abs(fdw-wa_t))
    assert abs(fdq-qa_t)<1e-5 and abs(fdw-wa_t)<1e-5
report.update(general_convex_checks=1000,general_convex_max_quantity_cross_error=max_qerr,general_convex_max_welfare_cross_error=max_werr)
(OUT/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
print('General convex extension:',max_qerr,max_werr)
