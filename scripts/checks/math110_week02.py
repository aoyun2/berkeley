"""Exact checks of numerical examples and answers in Math110 week2."""
import sympy as s
x,a=s.symbols('x a'); I=s.I
assert s.Matrix([[1,1,2],[0,1,1]])*s.Matrix([1,1,-1])==s.zeros(2,1)
assert s.expand(6+4*(x-1)+(x-1)**2)==x*x+2*x+3
u1,u2,w1,w2=[s.Matrix(v) for v in [(1,1,0),(0,1,1),(1,2,2),(2,2,1)]]
assert -u1+u2==w1-w2==s.Matrix([-1,0,1])
# All-field independence of u1,u2,w1: determinant is a unit over every field.
assert s.Matrix.hstack(u1,u2,w1).det()==1
assert s.Matrix.hstack(w1,w2).rank()==2
U=[(x-1)**k for k in (2,3,4)]
assert all(p.subs(x,1)==0 and s.diff(p,x).subs(x,1)==0 for p in U)
assert s.Matrix([[s.expand(p).coeff(x,k) for p in U] for k in range(5)]).rank()==3
u1,u2,w1,w2=[s.Matrix(v) for v in [(1,1,0,0),(0,1,1,0),(0,0,1,1),(1,0,0,-1)]]
M=s.Matrix.hstack(u1,u2,w1,w2)
assert M.det()!=0
assert M.inv()*s.Matrix([2,1,3,0])==s.Matrix([0,1,2,2])
assert u2+2*w1+2*w2==s.Matrix([2,1,3,0])
assert 3+5-8==0
assert 2+2-3==1
for n in range(1,8):
 assert s.eye(n).rank()==n
for v in (0,1): assert (v*v-v)%2==0
print('Week2 exact arithmetic, polynomial bases and exam decomposition passed.')
