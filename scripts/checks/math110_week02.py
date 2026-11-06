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


# Every additional displayed computation in the revised packet.
X,Y,Z,c=s.symbols('X Y Z c')
assert s.Matrix([[1,1],[0,1]])*s.Matrix([X-Y,Y]) == s.Matrix([X,Y])
v,w=s.Matrix([2,1,-3]),s.Matrix([1,-2,4])
assert 6*v+5*w == s.Matrix([17,-4,2])
assert -3*6+4*5 != 5
u,v,w=s.Matrix([2,3,1]),s.Matrix([1,-1,2]),s.Matrix([7,3,c])
assert s.Matrix.hstack(u,v,w).det() == 40-5*c
assert 2*u+3*v == w.subs(c,8)
v1,v2,v3,v4=[s.Matrix(q) for q in [(1,2),(3,6),(4,7),(5,9)]]
assert v2==3*v1 and v4==v1+v3
assert (4*Y-7*X)*v1+(2*X-Y)*v3 == s.Matrix([X,Y])
assert 3*s.Matrix([1,2,3])+2*s.Matrix([6,5,4]) == s.Matrix([15,16,17])
e1,e2,f2=s.Matrix([1,1]),s.Matrix([1,-1]),s.Matrix([0,1])
assert e1-f2 == s.Matrix([1,0])
assert (e1-e2)/2 == f2
u,v=s.Matrix([2,3,4]),s.Matrix([9,6,8])
assert -s.Rational(2,5)*u+s.Rational(1,5)*v == s.Matrix([1,0,0])
a_expr,b_expr,c_expr=(9*Z-8*X)/20,(2*X-Z)/10,Y-3*Z/4
assert (a_expr*u+b_expr*v+c_expr*s.Matrix([0,1,0])-s.Matrix([X,Y,Z])).applyfunc(s.simplify)==s.zeros(3,1)
u,v=s.Matrix([1,2]),s.Matrix([3,5])
assert (3*Y-5*X)*u+(2*X-Y)*v == s.Matrix([X,Y])
assert 19*u-5*v-s.Matrix([4,13]) == s.zeros(2,1)
assert s.Matrix([[1,7],[2,-5]]).det() == -19
assert s.Matrix([[5,4],[7,3]]).det() == -13
assert s.Matrix([[7,-4],[5,9]]).det() == 83
assert -Y*s.Matrix([1,-1,0])-Z*s.Matrix([1,0,-1]) == s.Matrix([-Y-Z,Y,Z])
for k in range(5):
 assert s.diff((x-a)**k,x,k).subs(x,a) == s.factorial(k)
assert all(s.diff(q,x).subs(x,5)==0 for q in [s.Integer(1),(x-5)**2,(x-5)**3])
v,u,w=s.Matrix([-1,0,1]),s.Matrix([1,1,0]),s.Matrix([1,2,2])
assert v+u == s.Matrix([0,1,1])
assert w-v == s.Matrix([2,2,1])
assert abs(s.Matrix.hstack(v,u,w).det()) == 1
print('Week2 exact arithmetic, polynomial bases, textbook examples and exam decomposition passed.')
