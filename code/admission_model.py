"""Exact active-set solutions for the R1 theoretical model. No firm data."""
import itertools
import numpy as np

def solve_qp(M,h,a=None,C=None,upper=None):
    """Max h'y-y'My/2, y>=0; optional one capacity or box upper bounds."""
    M=np.array(M,float);h=np.array(h,float);J=len(h);best=None
    if upper is not None:
        upper=np.array(upper,float)
        for states in itertools.product(range(3),repeat=J):
            free=[j for j,s in enumerate(states) if s==1];bound=[j for j,s in enumerate(states) if s!=1]
            y=np.array([upper[j] if s==2 else 0. for j,s in enumerate(states)])
            if free:y[free]=np.linalg.solve(M[np.ix_(free,free)],h[free]-M[np.ix_(free,bound)]@y[bound])
            g=h-M@y
            if np.any(y< -1e-8) or np.any(y>upper+1e-8):continue
            if any((s==0 and g[j]>1e-7) or (s==1 and abs(g[j])>1e-7) or (s==2 and g[j]<-1e-7) for j,s in enumerate(states)):continue
            val=h@y-.5*y@M@y
            if best is None or val>best[0]:best=(val,y,0.,states)
    else:
        a=np.ones(J) if a is None else np.array(a,float)
        for mask in itertools.product([False,True],repeat=J):
            S=np.flatnonzero(mask);y=np.zeros(J)
            for binding in [False,True] if C is not None else [False]:
                if binding and not len(S):continue
                nu=0.
                if len(S):
                    invh=np.linalg.solve(M[np.ix_(S,S)],h[S]);inva=np.linalg.solve(M[np.ix_(S,S)],a[S])
                    if binding:nu=(a[S]@invh-C)/(a[S]@inva)
                    y[S]=invh-nu*inva
                if nu< -1e-8 or np.any(y< -1e-8):continue
                if C is not None and a@y>C+1e-8:continue
                if binding and abs(a@y-C)>1e-7:continue
                g=h-M@y-nu*a
                if any((mask[j] and abs(g[j])>1e-7) or (not mask[j] and g[j]>1e-7) for j in range(J)):continue
                val=h@y-.5*y@M@y
                if best is None or val>best[0]:best=(val,y.copy(),max(nu,0),tuple(mask))
    if best is None:raise ValueError('No KKT solution')
    return best[1],best[2],best[3]

def allocation(h,V,K,n,a,gamma,C,kappa,beta,tolled=True,upper=None):
    h,V,K,n,a=map(lambda z:np.array(z,float),(h,V,K,n,a))
    D=np.diag(1/n);Q=V@np.linalg.solve(K,V.T)
    M=D+(gamma*np.outer(a,a) if tolled else 0)-beta/kappa*Q
    assert np.linalg.eigvalsh(D-Q/kappa).min()>0,'Strong concavity assumption failed'
    y,nu,active=solve_qp(M,h,a,C if tolled else None,upper if not tolled else None)
    z=beta/kappa*np.linalg.solve(K,V.T@y)
    A=a@y
    W=h@y+z@V.T@y-.5*y@D@y-.5*gamma*A*A-.5*kappa*z@K@z
    production_cost=.5*kappa*z@K@z
    H=D+(gamma*np.outer(a,a) if tolled else 0)
    y0,_,_=solve_qp(H,h,a,C if tolled else None,upper if not tolled else None)
    G0=h@y0-.5*y0@H@y0
    G=h@y+z@V.T@y-.5*y@H@y
    T=beta*(G-G0)
    R=T-production_cost
    rent=.5*gamma*A*A+nu*A if tolled else 0.
    return dict(y=y,z=z,A=A,nu=nu,W=W,R=R,T=T,production_cost=production_cost,G=G,G0=G0,Gamma=rent,q=sum(z),active=active)

def serial(s):
    return {k:(v.tolist() if isinstance(v,np.ndarray) else float(v) if isinstance(v,np.floating) else [bool(x) for x in v] if k=='active' else v) for k,v in s.items()}

if __name__=='__main__':
    p=dict(V=[[.5,.1],[.1,.4]],K=np.diag([4.,5.]),n=[1,1],a=[1,1],gamma=.5,C=20,kappa=1,beta=.5)
    for h in [[4,-1],[4,.5]]:
        print(h,serial(allocation(h=h,**p,tolled=False,upper=[10,10])))
        print('corrected',serial(allocation(h=h,**p)))
