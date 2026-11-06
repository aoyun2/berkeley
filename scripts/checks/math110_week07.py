"""Exact checks for every displayed numerical Week 7 example and HW answer."""
import sympy as s
x=s.symbols('x')
I=s.I

def pmat(p,A):
    return sum((c*A**int(j[0]) for j,c in s.Poly(p,x).terms()),s.zeros(A.rows)).applyfunc(s.simplify)
def mp(A):
    cols=[]
    for d in range(A.rows+1):
        c=s.Matrix(A**d).reshape(A.rows**2,1)
        if cols:
            B=s.Matrix.hstack(*cols)
            if B.row_join(c).rank()==B.rank():
                a=B.gauss_jordan_solve(-c)[0]
                return s.expand(x**d+sum(a[j]*x**j for j in range(d)))
        cols.append(c)
    raise AssertionError('degree bound failed')
def eig(A,v,l): assert (A*s.Matrix(v)-l*s.Matrix(v)).applyfunc(s.simplify)==s.zeros(A.rows,1)
def expectmp(A,p): assert s.expand(mp(A)-p)==0 and pmat(p,A)==s.zeros(A.rows)
A=s.Matrix([[1,2,3,4],[0,5,6,7],[0,0,8,9],[0,0,0,10]])
assert set(A.eigenvals())=={1,5,8,10}
D=s.zeros(4)
for j in range(1,4): D[j-1,j]=j
assert [s.diff(x**3,x,k) for k in range(5)]==[x**3,3*x*x,6*x,6,0]
expectmp(D,x**4)
A=s.Matrix([[1,2],[2,3]])
for sig in [-1,1]: eig(A,[2,1+sig*s.sqrt(5)],2+sig*s.sqrt(5))
R=s.Matrix([[0,-1],[1,0]])
for sig in [-1,1]: eig(R,[1,-sig*I],sig*I)
expectmp(R,x*x+1)
A=s.Matrix([[2,1,0],[0,5,3],[0,0,8]])
vecs=[[1,0,0],[1,3,0],[1,6,6]]
for v,l in zip(vecs,[2,5,8]): eig(A,v,l)
S=s.Matrix.hstack(*map(s.Matrix,vecs))
assert S*s.Matrix([s.Rational(1,6),-s.Rational(1,3),s.Rational(1,6)])==s.eye(3)[:,2]
assert A**100*s.eye(3)[:,2]==s.Matrix([2**100-2*5**100+8**100,6*8**100-6*5**100,6*8**100])/6
F=s.Matrix([[0,1],[1,1]])
for sig in [-1,1]:
    l=(1+sig*s.sqrt(5))/2
    eig(F,[1,l],l)
for n in range(15): assert s.simplify((((1+s.sqrt(5))/2)**n-((1-s.sqrt(5))/2)**n)/s.sqrt(5)-s.fibonacci(n))==0
P=s.Matrix([[s.Rational(1,2),s.Rational(1,4),0],[s.Rational(1,2),s.Rational(1,2),s.Rational(1,2)],[0,s.Rational(1,4),s.Rational(1,2)]])
pi=s.Matrix([s.Rational(1,4),s.Rational(1,2),s.Rational(1,4)])
u=s.Matrix([-1,0,1]); w=s.Matrix([1,-2,1])
for v,l in [(pi,1),(u,s.Rational(1,2)),(w,0)]: eig(P,v,l)
e1=s.eye(3)[:,0]
assert pi-u/2+w/4==e1
for k in range(1,10):
    assert P**k*e1==pi-u/2**(k+1)
    assert sum(map(abs,P**k*e1-pi))==s.Rational(1,2)**k
e=s.symbols('e',real=True)
Pe=s.Matrix([[1-e,e],[e,1-e]])
eig(Pe,[1,1],1); eig(Pe,[1,-1],1-2*e)
assert 1-2*s.Rational(1,100)==s.Rational(49,50)
A=s.Matrix([[2,1],[1,2]])
assert A*A==s.Matrix([[5,4],[4,5]])==4*A-3*s.eye(2)
expectmp(A,x*x-4*x+3)
C=s.Matrix([[0,0,0,0,-3],[1,0,0,0,6],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0]])
expectmp(C,x**5-6*x+3)
assert s.Matrix.hstack(*[C**j*s.eye(5)[:,0] for j in range(5)])==s.eye(5)
assert s.gcd(x**5-6*x+3,5*x**4-6)==1
assert s.Rational(5,8)**4==s.Rational(625,4096) and 3125!=24576
B=s.Matrix([[6,3,4],[0,6,2],[0,0,7]])
assert (B-6*s.eye(3))*(B-7*s.eye(3))==s.Matrix([[0,-3,6],[0,0,0],[0,0,0]])
expectmp(B,(x-6)**2*(x-7))
B=s.Matrix([[1,1],[0,1]])
expectmp(B,(x-1)**2)
q=x**4+x**3-x**2-5*x+4
assert s.expand((x-1)**2*(x*x+3*x+4)-q)==0
assert s.rem(x*(-x**3-x*x+x+5)/4-1,q,x)==0
for root in [1,(-3+I*s.sqrt(7))/2,(-3-I*s.sqrt(7))/2]: assert s.simplify(q.subs(x,root))==0
C=s.Matrix([[2,1,0],[0,2,0],[0,0,3]])
expectmp(C,(x-2)**2*(x-3))
assert (C-2*s.eye(3)).nullspace()==[s.Matrix([1,0,0])]
assert (C-3*s.eye(3)).nullspace()==[s.Matrix([0,0,1])]
assert (C-2*s.eye(3))*(C-3*s.eye(3))==s.Matrix([[0,-1,0],[0,0,0],[0,0,0]])
# Optional affine substitutions and exact interpolation-projector identities.
l,c=s.symbols('l c',nonzero=True)
for A in [R,B,C]:
    assert pmat(mp(A).subs(x,x+l),A-l*s.eye(A.rows))==s.zeros(A.rows)
    d=s.degree(mp(A),x)
    assert pmat(s.expand(c**d*mp(A).subs(x,x/c)),c*A)==s.zeros(A.rows)
roots=[s.Integer(1),s.Integer(3),s.Integer(5)]
ps=[s.prod((x-k)/(j-k) for k in roots if k!=j) for j in roots]
assert s.expand(sum(ps)-1)==0
for j,p in enumerate(ps):
    assert [p.subs(x,k) for k in roots]==[int(i==j) for i in range(3)]
    M=pmat(p,s.diag(*roots)); assert M*M==M
A=s.Matrix([[41,7],[-20,74]])
eig(A,[1,4],69); eig(A,[7,5],46)
assert s.Matrix([[1,7],[4,5]]).det()==-23
assert s.diag(8,5,5).eigenvals()=={8:1,5:2}
print('Week 7 exact matrix relations, eigenpairs, powers, stochastic formulas, Fibonacci, minimal polynomials, inverse and interpolation checks passed.')
