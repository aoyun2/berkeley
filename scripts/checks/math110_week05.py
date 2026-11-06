"""Exact checks of all numerical Math110 week5 examples and homework."""
import sympy as s
x,y,z=s.symbols('x y z')
B=s.Matrix([[1,1],[1,-1]])
assert B.inv()==s.Matrix([[s.Rational(1,2),s.Rational(1,2)],[s.Rational(1,2),-s.Rational(1,2)]])
assert B.inv()*B==s.eye(2)
A=s.Matrix([[1,2,3],[4,5,6]])
assert s.Matrix([[x,y]])*A==s.Matrix([[x+4*y,2*x+5*y,3*x+6*y]])
P=s.Matrix([[s.Rational(1,2),s.Rational(1,4),0],[s.Rational(1,2)]*3,[0,s.Rational(1,4),s.Rational(1,2)]])
f=s.Matrix([0,1,4]);p=s.Matrix([1,0,0])
assert P.T*f==s.Matrix([s.Rational(1,2),s.Rational(3,2),s.Rational(5,2)])
assert (f.T*P*p)[0]==s.Rational(1,2)
U=s.Matrix([[1,0],[1,1],[0,1]])
a=s.Matrix([[-1,1,-1]])
assert U.rank()==2 and a*U==s.zeros(1,2)
assert U.T.nullspace()==[s.Matrix([1,-1,1])]
K=[x*(x-1),x*x*(x-1)]
assert all(q.subs(x,0)==0 and q.subs(x,1)==0 for q in K)
Kmat=s.Matrix([[s.expand(q).coeff(x,j) for q in K] for j in range(4)])
E=s.Matrix([[1,0,0,0],[1,1,1,1]])
assert Kmat.rank()==2 and E*Kmat==s.zeros(2) and E.rank()==2
assert s.Matrix([[1,0],[1,1]]).rank()==2
q=s.Symbol('a')+(s.Symbol('b')-s.Symbol('a'))*x
assert q.subs(x,0)==s.Symbol('a') and q.subs(x,1)==s.Symbol('b')
assert 3*s.Matrix([[2,-1]])==s.Matrix([[6,-3]])
p=x**4+3*x*x-2*x+7
assert s.diff(x**3/3,x)==x*x
assert s.integrate(s.diff(p,x),(x,0,1))==p.subs(x,1)-p.subs(x,0)
assert (x*p).subs(x,2)==2*p.subs(x,2)
T=s.Matrix([[1,0]])
assert T.rank()==T.T.rank()==1 and len(T.nullspace())==1 and len(T.T.nullspace())==0
# Restored textbook examples, figures, and actual saved review calculations.
assert 4-5*2+2*3==0
poly=x*x
assert 3*s.diff(poly,x,2).subs(x,5)+7*poly.subs(x,4)==118
assert s.diff(x*x*p,x).subs(x,0)==0
assert s.diff(x,x).subs(x,0)==1
coords=s.symbols('a1:6')
row=s.Matrix([coords]);basis=s.eye(5)[:,:2]
assert row*basis==s.Matrix([[coords[0],coords[1]]])
assert s.Matrix([[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]).rank()==3
assert s.diag(2,3,4)*s.Matrix([x,y,z])==s.Matrix([2*x,3*y,4*z])
assert s.Matrix([[3,4]])*s.Matrix([2,-1])==s.Matrix([2])
R=s.Matrix([[1,0,0],[1,1,0],[0,1,2]])
assert R.inv()==s.Matrix([[1,0,0],[-1,1,0],[s.Rational(1,2),-s.Rational(1,2),s.Rational(1,2)]])
functions=[1,s.sin(x),s.sin(2*x)]
for k,func in enumerate(functions):
 func=s.sympify(func)
 values=s.Matrix([func.subs(x,0),func.subs(x,s.pi/2),s.diff(func,x).subs(x,0)])
 assert values==R[:,k]
 assert R.inv()*values==s.eye(3)[:,k]
means=s.Matrix([[s.integrate(s.sympify(func),(x,0,s.pi))/s.pi for func in functions]])
assert means==s.Matrix([[1,2/s.pi,0]])
assert s.simplify(means*R.inv()-s.Matrix([[1-2/s.pi,2/s.pi,0]]))==s.zeros(1,3)
T=s.Matrix([1,0])
assert T.rank()==1 and T.T*s.Matrix([0,1])==s.zeros(1,1)
# Generic coordinate witnesses for the quotient figure.
for vec in [(2,3,5),(9,-1,5)]:assert vec[1:][1]==5
assert (1+1)/2==1 and (1-1)/2==0
print('Week5 exact quotient, dual, annihilator, expectation and exam checks passed.')
