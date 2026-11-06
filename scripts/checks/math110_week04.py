"""Exact checks for Math110 week4 matrices, interpolation, products and cosets."""
import sympy as s
x,t,a,b,c,d=s.symbols('x t a b c d')
A=s.Matrix([[a,b],[c,d]]);B=s.Matrix([[d,-b],[-c,a]])
assert A*B==B*A==(a*d-b*c)*s.eye(2)
assert s.Matrix([[1,2]])*s.Matrix([1-2*t,t])==s.ones(1,1)
assert s.Matrix([[1,2]])*s.Matrix([-2,1])==s.zeros(1,1)
T=s.Matrix([[1,1],[0,1]]);Ti=s.Matrix([[1,-1],[0,1]])
assert T*Ti==Ti*T==s.eye(2)
assert s.expand((x-1)*(x-2)/2-2*x*(x-2)+s.Rational(5,2)*x*(x-1))==1+x*x
assert s.diff(x*x+5*x+7,x,2)==2
S=s.Matrix([[1,1],[0,1]]);T=s.diag(2,1)
assert S.inv()*T.inv()==s.Matrix([[s.Rational(1,2),-1],[0,1]])
assert (S*T).inv()==s.Matrix([[s.Rational(1,2),-s.Rational(1,2)],[0,1]])
Q=s.Matrix([[4,5],[2,3]])
assert Q.inv()==s.Matrix([[s.Rational(3,2),-s.Rational(5,2)],[-1,2]])
assert Q.inv()*s.diag(1,0)*Q==s.Matrix([[6,s.Rational(15,2)],[-4,-5]])
assert s.Matrix([[2,1],[5,3]]).inv()==s.Matrix([[3,-1],[-5,2]])
A=s.Matrix([[1,s.I],[s.I,-1]])
assert A.det()==0 and A*s.Matrix([s.I,-1])==s.zeros(2,1)
A=s.Matrix([[1,2],[3,1]])
assert A.det()%5==0 and all(z%5==0 for z in A*s.Matrix([3,1]))
assert s.diag(1,0).rank()==s.diag(0,1).rank()==1
assert s.diag(1,0)*s.diag(0,1)==s.zeros(2)
M=s.Matrix([[1,1,0],[0,1,1],[1,0,1]])
B=s.Matrix([[1,1,1],[0,1,1],[0,0,1]])
assert M*B==s.Matrix([[1,2,2],[0,1,2],[1,1,2]]) and M.rank()==3
assert s.diff(x**3/3,x)==x*x
assert s.Matrix([1,2])+s.Matrix([3,-1])==s.Matrix([4,1])
assert 2*s.Matrix([1,2])==s.Matrix([2,4])
p=x**3+2*x*x-4*x+7
Tp=s.integrate(p.subs(x,t),(t,0,x+1))
assert s.expand(s.diff(Tp,x)-p.subs(x,x+1))==0
q=(x+1)*(x*x+2)
assert s.expand(s.integrate(s.diff(q,x).subs(x,t-1),(t,0,x+1))-q)==0
Jp=s.integrate(p.subs(x,t),(t,-1,x))
assert s.expand(s.diff(Jp,x).subs(x,x-1)-p.subs(x,x-1))==0
assert s.expand(s.integrate(s.diff(p,x).subs(x,t),(t,0,x))-(p-p.subs(x,0)))==0
print('Week4 exact inverse, coordinate, polynomial, finite-field, and coset checks passed.')
