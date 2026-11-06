"""Exact arithmetic checks for the 2026-08-31 handout and solutions."""
from itertools import product
from sympy import I, Matrix, Poly, Rational, expand, integrate, simplify, sqrt, symbols
x=symbols('x')
assert expand((1+I)**3)==-2+2*I
assert expand((5+I)*(4+3*I))==17+19*I
assert simplify(1/(3+4*I)-(3-4*I)/25)==0
assert expand((2+I)**3)==2+11*I
assert expand((2-I)**3)==2-11*I
assert 4**3-15*4-4==0
z=(-1+sqrt(3)*I)/2
assert simplify(z**2-(-1-sqrt(3)*I)/2)==0
assert simplify(z**3)==1
assert integrate(x-Rational(1,2),(x,0,1))==0
assert Poly((x+1)**8,x,modulus=2)==Poly(x**8+1,x,modulus=2)
assert Poly((x+1)**8,x).all_coeffs()==[1,8,28,56,70,56,28,8,1]
for power in (2,4,8):
 assert Poly((x+1)**power,x,modulus=2)==Poly(x**power+1,x,modulus=2)
for a,b,c in product(range(2),repeat=3):
 assert ((a+b)+c)%2 == (a+(b+c))%2
 assert (a*(b+c))%2 == (a*b+a*c)%2
assert Matrix([3,3])+Matrix([1,-1])==Matrix([4,2])
t,s,X,Y=symbols('t s X Y')
assert simplify((X+Y)/2+(X-Y)/2-X)==0
assert simplify((X+Y)/2-(X-Y)/2-Y)==0
assert Matrix([1,0])+Matrix([0,1])+Matrix([-1,-1])==Matrix([0,0])
fib=[0,1]
for _ in range(5): fib.append(sum(fib[-2:]))
assert fib==[0,1,1,2,3,5,8]
# Exhaustively check the image/inverse-image identities on all maps between
# sets with at most three elements, including empty sets where maps exist.
for n in range(4):
 for m in range(4):
  X,Y=set(range(n)),set(range(m))
  for vals in product(range(m),repeat=n):
   def image(U): return {vals[u] for u in U}
   def pre(V): return {u for u in X if vals[u] in V}
   for mask in range(1<<m):
    V={i for i in Y if mask>>i&1}
    assert image(pre(V))==V&image(X)
    assert (image(pre(V))==V)==(V<=image(X))
   for mask in range(1<<n):
    U={i for i in X if mask>>i&1}
    assert U<=pre(image(U))
    assert (pre(image(U))==U)==(not image(U)&image(X-U))
print('Week 1 exact arithmetic, F2 identities and finite-set checks passed.')
