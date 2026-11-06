"""Exact verification of all numerical Math110 week3 examples and answers."""
import sympy as s
from itertools import product
x,t,theta=s.symbols('x t theta',real=True)
I=s.I
P=s.Matrix([[0,0],[0,1]]);N=s.Matrix([[0,1],[0,0]])
R=s.Matrix([[s.cos(theta),-s.sin(theta)],[s.sin(theta),s.cos(theta)]])
assert R.subs(theta,-s.pi/2)*P==N and N*N==s.zeros(2)
assert P*N==s.zeros(2) and N*P==N
f=x**4+3*x+1
assert s.expand(s.diff(x*f,x)-x*s.diff(f,x))==f
B=s.Matrix([[1,1],[1,-1]])
T=s.Matrix([[s.Rational(1,2),s.Rational(1,2)],[1,-1]])
assert T*B==s.diag(1,2)
A=s.Matrix([[1+I,3+2*I,4],[5,I,2+I]])
Q=s.Matrix([[4-2*I,5,1],[3,2,I]])
assert s.simplify(A+Q)==s.Matrix([[5-I,8+2*I,5],[8,2+I,2+2*I]])
assert s.simplify((1+I)*A)==s.Matrix([[2*I,1+5*I,4+4*I],[5+5*I,-1+I,1+3*I]])
B=s.Matrix([[1,1,0],[1,0,1],[0,1,1]])
assert B.rank()==3 and B*s.Matrix([0,1,2])==s.Matrix([1,2,3])
E=s.Matrix([[1,z,z*z,z**3] for z in [1,I,-1,-I]])
assert E==s.Matrix([[1,1,1,1],[1,I,-1,-I],[1,-1,1,-1],[1,-I,-1,I]])
assert E*s.Matrix([1,2,1,0])==s.Matrix([4,2*I,0,-2*I])
assert s.Matrix([[1,2,3],[2,3,4]])*s.Matrix([5,7,9])==s.Matrix([46,67])
D=s.Matrix([[0,1,0,0],[0,0,2,0],[0,0,0,3]])
J=s.Matrix([[0,0,0],[1,0,0],[0,s.Rational(1,2),0],[0,0,s.Rational(1,3)]])
assert J*D==s.diag(0,1,1,1) and D*J==s.eye(3)
C=s.Matrix([[1,0],[0,1],[1,1]]);R=s.Matrix([[1,0,2],[0,1,3]])
A=C*R
assert A==s.Matrix([[1,0,2],[0,1,3],[1,1,5]]) and A.rank()==2
assert A*s.Matrix([-2,-3,1])==s.zeros(3,1)
P=s.Matrix([[s.Rational(1,2),s.Rational(1,4),0],[s.Rational(1,2)]*3,[0,s.Rational(1,4),s.Rational(1,2)]])
p=s.Matrix([1,0,0])
for expected in [[s.Rational(1,2),s.Rational(1,2),0],[s.Rational(3,8),s.Rational(1,2),s.Rational(1,8)],[s.Rational(5,16),s.Rational(1,2),s.Rational(3,16)]]:
 p=P*p;assert p==s.Matrix(expected)
pi=s.Matrix([s.Rational(1,4),s.Rational(1,2),s.Rational(1,4)])
assert P*pi==pi
D4=s.Matrix([[s.diff(x**j,x).coeff(x,k) for j in range(5)] for k in range(5)])
assert D4.rank()==4 and D4.nullspace()==[s.Matrix([1,0,0,0,0])]
S=s.Matrix([[1]*5,list(range(5))]);assert S.rank()==2
A=s.Matrix([[s.expand(x*x*s.diff(x**j,x)+x**j).coeff(x,k) for j in range(4)] for k in range(5)])
assert A==s.Matrix([[1,0,0,0],[0,1,0,0],[0,1,1,0],[0,0,2,1],[0,0,0,3]]) and A.rank()==4
sols=[v for v in product(range(2),repeat=4) if sum(v)%2==1 and (v[0]+v[2])%2==0]
assert sols==[(0,0,0,1),(0,1,0,0),(1,0,1,1),(1,1,1,0)]
T4=s.Matrix([[0,0,1,0],[0,0,0,1],[0,0,0,0],[0,0,0,0]])
assert T4.columnspace()==T4.nullspace()
print('Week3 exact matrix, polynomial, probability, and finite-field checks passed.')
