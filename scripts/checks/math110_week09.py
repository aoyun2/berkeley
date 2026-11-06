"""Exact Week 9 trace, inner-product, norm, attention and HW checks."""
import sympy as s
x=s.symbols('x',real=True)
I=s.I
inner=lambda u,v: (s.Matrix(u).T*s.conjugate(s.Matrix(v)))[0]
sq=lambda u:s.simplify(inner(u,u))
A=s.Matrix([[1,2,3],[4,5,6],[7,8,9]])
assert s.trace(A)==15
A=s.Matrix([[1,1,1],[1,2,4],[1,3,9]])
assert s.trace(A)==12 and A.charpoly().all_coeffs()[1]==-12
B=s.Matrix([[3,-1,-2],[3,2,-3],[1,2,0]])
assert s.trace(B)==5
for l,v in [(1,[1,0,1]),(2+3*I,[I,1+I,1]),(2-3*I,[-I,1-I,1])]:
    assert (B*s.Matrix(v)-l*s.Matrix(v)).applyfunc(s.simplify)==s.zeros(3,1)
z=s.symbols('z')
assert s.expand(B.charpoly(z).as_expr()-(z-1)*((z-2)**2+9))==0
A=s.Matrix([[0,1],[0,0]]); B=s.Matrix([[0,0],[1,0]])
assert A*B==s.diag(1,0) and B*A==s.diag(0,1)
assert A*B-B*A==s.diag(1,-1) and s.trace(A*B-B*A)==0
C=s.diag(1,0)
assert s.trace(A*B*C)==1 and s.trace(A*C*B)==0
assert s.diag(1,-1)**2==s.eye(2)
assert inner([I,1],[I,1])==2 and (I**2+1)==0
assert inner([1,I],[1,I])==2
assert (s.Matrix([1,I]).T*s.diag(1,2)*s.conjugate(s.Matrix([1,I])))[0]==3
assert inner([1],[I])==-I
assert s.integrate(x,(x,0,1))==s.Rational(1,2)
assert s.integrate(x*x,(x,0,1))==s.Rational(1,3)
derivinner=lambda p,q:p.subs(x,0)*q.subs(x,0)+s.integrate(s.diff(p,x)*s.diff(q,x),(x,-1,1))
assert [derivinner(p,p) for p in [s.Integer(1),x,x*x]]==[1,2,s.Rational(8,3)]
for k in range(7):assert s.integrate(x**k*s.exp(-x),(x,0,s.oo))==s.factorial(k)
assert [s.integrate(p*q*s.exp(-x),(x,0,s.oo)) for p,q in [(1,x),(x,x),(x*x,x*x)]]==[1,2,24]
assert inner([1,1],[1,-1])==0 and inner([1,1],[1,1])==2
assert s.integrate(s.sin(x),(x,0,s.pi))==2
val=s.Integral(s.sqrt(s.sin(x)),(x,0,s.pi)).evalf(20)
assert abs(val-s.Float('2.3962804694711844',20))<s.Float('1e-15')
assert val<s.sqrt(2*s.pi) and round(float(s.sqrt(2*s.pi)),3)==2.507
# Polarization for a symbolic complex pair, using first-position linearity.
a,b,c,d,e,f,g,h=s.symbols('a b c d e f g h',real=True)
u=s.Matrix([a+I*b,c+I*d]);v=s.Matrix([e+I*f,g+I*h])
assert s.simplify(sq(u+v)+sq(u-v)-2*sq(u)-2*sq(v))==0
pol=(sq(u+v)-sq(u-v)+I*sq(u+I*v)-I*sq(u-I*v))/4
assert s.simplify(pol-inner(u,v))==0
assert s.Abs(1+I)==s.sqrt(2)
assert s.acos(1/s.sqrt(2))==s.pi/4
# Exact toy softmax and causal matrices; decimals only compare reported rounding.
sc=s.Matrix([s.sqrt(2),0,-1/s.sqrt(2)])
weights=sc.applyfunc(s.exp);weights=weights/sum(weights)
assert s.simplify(sum(weights)-1)==0
assert [round(float(w),3) for w in weights]==[.734,.178,.088]
Q=s.Matrix([[0,1]]);K=Q;V=Q
assert Q.T*K==s.Matrix([[0,0],[0,1]])
A=s.Matrix([[1,0],[1/(1+s.E),s.E/(1+s.E)]])
assert (A*s.ones(2,1)).applyfunc(s.simplify)==s.ones(2,1)
assert A[0,1]==0 and V*A.T==s.Matrix([[0,s.E/(1+s.E)]])
t=s.symbols('t',real=True)
fun=t*s.exp(t*t)/(1+s.exp(t*t))
delta=s.simplify(fun.subs(t,2)-2*fun.subs(t,1))
assert s.simplify(delta-2*s.E*(s.exp(3)-1)/((1+s.E)*(1+s.exp(4))))==0
scores=s.Matrix([s.sqrt(2),0,-1/s.sqrt(2)])
shifted=(scores-s.ones(3,1)*s.sqrt(2)).applyfunc(s.exp)
assert (shifted/sum(shifted)-weights).applyfunc(s.simplify)==s.zeros(3,1)
# HW trace realizations: maximal 2-block size2; all -1 blocks have size1.
def J(r,l):
 A=l*s.eye(r)
 for j in range(1,r):A[j-1,j]=1
 return A
forms=[s.diag(J(2,2),-1,-1,-1),s.diag(J(2,2),2,-1,-1),s.diag(J(2,2),J(2,2),-1)]
assert [s.trace(A) for A in forms]==[1,4,7]
for A in forms:
 N=A-2*s.eye(5);M=A+s.eye(5)
 assert N**2*M==s.zeros(5) and N*M!=s.zeros(5)
 assert A.eigenvals()[2]+A.eigenvals()[-1]==5
assert [(s.integrate(x**j*x**k,(x,-1,1))) for j,k in [(0,0),(1,1),(2,2),(0,1),(1,2),(0,2)]]==[2,s.Rational(2,3),s.Rational(2,5),0,0,s.Rational(2,3)]
v=s.Matrix([1+I,2-I]);w=s.Matrix([3,I])
T=w*s.conjugate(v).T
assert s.simplify(s.trace(T)-inner(w,v))==0
assert (1+2+3+4)*(s.Integer(1)+s.Rational(1,2)+s.Rational(1,3)+s.Rational(1,4))==s.Rational(125,6)>16
assert (2*4)*(s.Rational(1,2)*4)==16
print('Week 9 exact traces/eigenpairs, inner products/integrals, polarization, attention matrices/weights and all HW/practice computations passed.')
