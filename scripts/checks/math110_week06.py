"""Exact verification of Math110 week6 eigenvalue and PageRank computations."""
import sympy as s
x,t,lam=s.symbols('x t lam');I=s.I
R=s.Matrix([[0,-1],[1,0]]);N=s.Matrix([[0,1],[0,0]])
assert R*R==-s.eye(2) and N*N==s.zeros(2)
assert R*s.Matrix([1,-I])==I*s.Matrix([1,-I])
assert R*s.Matrix([1,I])==-I*s.Matrix([1,I])
assert s.Matrix([[7,0,3],[3,6,9],[0,-6,0]])*s.Matrix([3,1,-1])==6*s.Matrix([3,1,-1])
P=s.Matrix([[s.Rational(1,2),s.Rational(1,4),0],[s.Rational(1,2)]*3,[0,s.Rational(1,4),s.Rational(1,2)]])
pi=s.Matrix([s.Rational(1,4),s.Rational(1,2),s.Rational(1,4)])
assert P*pi==pi
assert (1+x*x).subs(x,I*t)==1-t*t
for j in range(1,8):assert s.diff(s.sin(j*x),x,2)==-j*j*s.sin(j*x)
A=s.diag(1,2);v=s.Matrix([1,1]);assert (A-s.eye(2))*(A-2*s.eye(2))*v==s.zeros(2,1)
assert s.Matrix.hstack(v,A*v).rank()==2
for lam0 in [(1+s.sqrt(5))/2,(1-s.sqrt(5))/2]:
 F=s.Matrix([[0,1],[1,1]]);v=s.Matrix([1,lam0])
 assert s.simplify(F*v-lam0*v)==s.zeros(2,1)
assert s.expand(R.charpoly(t).as_expr())==t*t+1
J=s.Matrix([[1,1],[0,1]])
assert J.charpoly(t).as_expr()==t*t-2*t+1
assert (J-s.eye(2)).nullspace()==[s.Matrix([1,0])]
for M in [s.Matrix([[1,0],[0,0]]),s.Matrix([[0,1],[1,0]]),s.Matrix([[0,0],[0,1]])]:assert M.T==M
M=s.Matrix([[0,1],[-1,0]]);assert M.T==-M
P2=s.Matrix([[0,1],[1,0]]);restart=s.Matrix([1,0]);alpha=s.Rational(1,2)
r=(s.eye(2)-alpha*P2).inv()*(1-alpha)*restart
assert r==s.Matrix([s.Rational(2,3),s.Rational(1,3)])
G=alpha*P2+(1-alpha)*restart*s.ones(1,2)
assert G==s.Matrix([[s.Rational(1,2),1],[s.Rational(1,2),0]]) and G*r==r
r1=G*restart;r2=G*r1
assert r1==s.Matrix([s.Rational(1,2),s.Rational(1,2)]) and r2==s.Matrix([s.Rational(3,4),s.Rational(1,4)])
assert sum(abs(z) for z in r1-r)==s.Rational(1,3)
assert sum(abs(z) for z in r2-r)==s.Rational(1,6)
P7=s.Matrix([[s.Rational(1,2),s.Rational(1,2),0],[s.Rational(1,2),0,s.Rational(1,2)],[0,s.Rational(1,2),s.Rational(1,2)]])
p=s.ones(3,1)/3;assert P7*p==p and (P7-s.eye(3)).rank()==2
assert s.diff(s.exp(lam*x),x)==lam*s.exp(lam*x)
a,b,c,d=s.symbols('a b c d');A=s.Matrix([[a,b],[c,d]])
assert s.expand((t*s.eye(2)-A).det()-(t*t-(a+d)*t+a*d-b*c))==0
assert s.expand(((1+s.I)/s.sqrt(2))**2)==s.I
assert s.expand(7*x*x-3*s.diff(x*x,x)+5*s.diff(x*x,x,2))==7*x*x-6*x+10
assert G*s.Matrix([1,-1])==-s.Matrix([1,-1])/2
assert s.Rational(2,3)*s.Rational(1,2)==s.Rational(1,3)
print('Week6 exact eigenvectors, polynomial identities, derivatives, stationary distributions and PageRank checks passed.')
