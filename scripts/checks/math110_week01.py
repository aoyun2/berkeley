"""Exact arithmetic checks for the 2026-08-31 handout and solutions."""
from itertools import product
from sympy import I, Matrix, Poly, Rational, conjugate, expand, integrate, simplify, sqrt, symbols, diff, re, solve_univariate_inequality, Interval, Union
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
 assert ((a*b)*c)%2 == (a*(b*c))%2
 assert (a+b)%2 == (b+a)%2
 assert (a*b)%2 == (b*a)%2
 assert (a+0)%2 == a and (a*1)%2 == a
 assert (a+a)%2 == 0
 assert (a*(b+c))%2 == (a*b+a*c)%2
assert Matrix([3,3])+Matrix([1,-1])==Matrix([4,2])
t,s,X,Y=symbols('t s X Y')
assert simplify((X+Y)/2+(X-Y)/2-X)==0
assert simplify((X+Y)/2-(X-Y)/2-Y)==0
assert Matrix([1,0])+Matrix([0,1])+Matrix([-1,-1])==Matrix([0,0])
fib=[0,1]
for _ in range(5): fib.append(sum(fib[-2:]))
assert fib==[0,1,1,2,3,5,8]
# Every newly displayed numeric or symbolic calculation in the regenerated packet.
assert expand((1+I)**2) == 2*I
assert expand((2+I)**2) == 3+4*I
assert expand((2-I)**2) == 3-4*I
assert expand((3+4*I)*(3-4*I)) == 25
assert simplify((3+4*I)*(Rational(3,25)-Rational(4,25)*I)) == 1
assert I**11 == -I
assert 2*Matrix([1,3])+Matrix([4,-1]) == Matrix([6,5])
assert expand(2*(1+I)-(3-I)) == -1+3*I
assert 2*3+1 == 7
assert -Matrix([2,-3]) == Matrix([-2,3])
# Complex laws, including the full associativity-coordinate expansion.
a,b,c,d,e,f = symbols('a b c d e f', real=True)
w,z,t = a+b*I,c+d*I,e+f*I
assert expand(conjugate(w+z)-conjugate(w)-conjugate(z)) == 0
assert expand(conjugate(w*z)-conjugate(w)*conjugate(z)) == 0
triple = (a*c*e-a*d*f-b*c*f-b*d*e) + I*(a*c*f+a*d*e+b*c*e-b*d*f)
assert expand((w*z)*t-triple) == 0
assert expand(w*(z*t)-triple) == 0
# The arrow example used in the handout and all equality/strictness cases.
arrow={'a':'p','b':'p','c':'q','d':'q'}
inputs=set(arrow)
img=lambda U: {arrow[u] for u in U}
pre=lambda V: {u for u in inputs if arrow[u] in V}
assert img({'a','c'}) == {'p','q'}
assert pre({'q','r'}) == {'c','d'}
assert img(pre({'q','r'})) == {'q'}
assert pre(img({'a','c'})) == inputs
assert img(pre({'p'})) == {'p'}
assert pre(img({'a','b'})) == {'a','b'}
# Squaring preimage shortcut: both real intervals are required.
r=symbols('r', real=True)
assert solve_univariate_inequality(r**2>=1,r, relational=False).intersect(
 solve_univariate_inequality(r**2<=4,r, relational=False)) == Union(Interval(-2,-1),Interval(1,2))
# Recurrence entries from general initial values, and concrete subspace equations.
p,q,alpha,rr,ss = symbols('p q alpha rr ss')
seq=[p,q]
for _ in range(4): seq.append(expand(seq[-2]+seq[-1]))
assert seq == [p,q,p+q,p+2*q,2*p+3*q,3*p+5*q]
assert alpha*Matrix([rr,-rr])+Matrix([ss,-ss]) == Matrix([alpha*rr+ss,-alpha*rr-ss])
assert alpha*Matrix([2*rr,rr])+Matrix([2*ss,ss]) == Matrix([2*(alpha*rr+ss),alpha*rr+ss])
Xcoord,Ycoord=symbols('Xcoord Ycoord')
assert Matrix([0,Ycoord-Xcoord])+Matrix([Xcoord,Xcoord]) == Matrix([Xcoord,Ycoord])
assert Matrix([1,0])+Matrix([0,1])+Matrix([0,0]) == Matrix([0,0])+Matrix([0,0])+Matrix([1,1])
# Added after the independent review: field equation and exact LADR examples.
a_nonzero=symbols('a_nonzero', nonzero=True)
b_scalar=symbols('b_scalar')
assert simplify(a_nonzero*(b_scalar/a_nonzero)-b_scalar) == 0
assert expand((a_nonzero+b_scalar*I)/a_nonzero-(1+b_scalar/a_nonzero*I)) == 0
assert 2*Rational(1,2) == 1
assert diff((x-2)**2,x) == 2*(x-2)
assert diff((x-2)**2,x).subs(x,2) == 0
assert re(I*I) == -1 and re(I)*re(I) == 0
A,B,C,D,X4,Y4,Z4=symbols('A B C D X4 Y4 Z4')
assert Matrix([A,A,B,B])+Matrix([C,C,C,D]) == Matrix([A+C,A+C,B+C,B+D])
assert Matrix([X4,X4,Y4,Y4])+Matrix([0,0,0,Z4-Y4]) == Matrix([X4,X4,Y4,Z4])
# Coordinate formula used for closure under a complex scalar in C^infinity.
a_real,b_real,xn,yn,sn,tn=symbols('a_real b_real xn yn sn tn', real=True)
assert expand((a_real+b_real*I)*(xn+yn*I)+(sn+tn*I)
 -((a_real*xn-b_real*yn+sn)+I*(a_real*yn+b_real*xn+tn))) == 0
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
# Visual discovery sequences: failed reciprocal, cancellation, normalization,
# and the unique direct-sum trial. These are mathematical checks of the figures.
assert expand((3+4*I)*Rational(1,3)) == 1+Rational(4,3)*I
assert 3*(-4)+4*3 == 0 and 3*3-4*(-4) == 25
assert Rational(9,25)+Rational(16,25) == 1
assert -Rational(12,25)+Rational(12,25) == 0
for trial,rem in [(1,[3,1]),(2,[2,0]),(3,[1,-1])]:
 assert Matrix([trial,trial])+Matrix(rem) == Matrix([4,2])
 assert (sum(rem)==0) == (trial==3)
 assert trial+trial+sum(rem) == 6
for diagonal in [Rational(0), Rational(1,2), Rational(1)]:
 assert Matrix([1-diagonal,0])+Matrix([0,1-diagonal])+Matrix([diagonal,diagonal]) == Matrix([1,1])
diagonal=symbols('diagonal', real=True)
assert Matrix([1-diagonal,0])+Matrix([0,1-diagonal])+Matrix([diagonal,diagonal]) == Matrix([1,1])
print('Week 1 exact arithmetic, F2 identities and finite-set checks passed.')
