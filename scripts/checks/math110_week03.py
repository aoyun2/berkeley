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


# Additional literal textbook examples and compact-figure coordinates.
assert s.integrate(1+2*x,(x,0,1)) == 2
assert s.expand(s.diff(x*x*f,x)-x*x*s.diff(f,x)-2*x*f) == 0
ss,tt,U,V=s.symbols('ss tt U V')
phi=s.Matrix([[1,2,3]])
assert phi*s.Matrix([-2*ss-3*tt,ss,tt]) == s.zeros(1,1)
assert s.Matrix([[2,0],[0,5],[1,1]])*s.Matrix([U/2,V/5]) == s.Matrix([U,V,U/2+V/5])
Brect=s.Matrix([[1,3],[2,5],[7,9]])
assert Brect[:,0] == s.Matrix([1,2,7]) and Brect[:,1] == s.Matrix([3,5,9])
Acol=s.Matrix([[1,2],[3,4],[5,6]])
assert Acol*s.Matrix([5,1]) == 5*Acol[:,0]+Acol[:,1] == s.Matrix([7,19,31])
Arank=s.Matrix([[4,7,1,8],[3,5,2,9]])
assert Arank.rank()==2 and Arank[:,:2].det()==-1
assert s.Matrix([[5,-7],[3,8],[-4,2]]).T == s.Matrix([[5,3,-4],[-7,8,2]])
assert s.Matrix([[1,0,1],[0,1,-1]])*s.Matrix([2,3,1]) == s.Matrix([3,2])
assert s.Matrix([[0,0],[0,1]])*s.Matrix([1,2]) == s.Matrix([0,2])
assert N*s.Matrix([1,2]) == s.Matrix([2,0])
for k in range(7):
 assert s.diff(x**(k+1)/s.Integer(k+1),x) == x**k
assert all(sum(P[:,j])==1 for j in range(3)) and all(z>=0 for z in P)
assert s.Matrix([[1,2]])*s.Matrix([3,4]) == s.Matrix([11])
# Literal LADR 3.23, 3.42 and 3.45 examples restored in the idea revision.
Acount=s.Matrix([[7,s.pi,0,1],[97,3,2,0],[0,1,6,7]])
assert Acount.shape==(3,4) and Acount.rank()==3 and len(Acount.nullspace())==1
assert s.Matrix([[1,2],[3,4],[5,6]])*s.Matrix([[6,5,4,3],[2,1,0,-1]])==s.Matrix([[10,7,4,1],[26,19,12,5],[42,31,20,9]])
Arow=s.Matrix([[8,4,5],[1,9,7]])
assert Arow[1,:]==s.Matrix([[1,9,7]]) and Arow[:,1]==s.Matrix([4,9])
print('Week3 exact matrix, polynomial, probability, textbook and finite-field checks passed.')
