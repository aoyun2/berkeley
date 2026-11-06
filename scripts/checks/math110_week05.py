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
print('Week5 exact quotient, dual, annihilator, expectation and exam checks passed.')
