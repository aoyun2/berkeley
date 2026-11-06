"""Exact Week 8 checks: every source matrix, kernel, block datum and answer."""
import sympy as s
x=s.symbols('x')
def J(r,l):
    A=l*s.eye(r)
    for j in range(1,r): A[j-1,j]=1
    return A
def nulls(A,ks): return [A.rows-(A**k).rank() for k in ks]
def pmat(p,A):
    return sum((c*A**j[0] for j,c in s.Poly(s.expand(p),x).terms()),s.zeros(A.rows)).applyfunc(s.simplify)
def mp(A):
    cols=[]
    for d in range(A.rows+1):
        col=(A**d).reshape(A.rows**2,1)
        if cols:
            B=s.Matrix.hstack(*cols)
            if B.row_join(col).rank()==B.rank():
                c=B.gauss_jordan_solve(-col)[0]
                return s.expand(x**d+sum(c[j]*x**j for j in range(d)))
        cols.append(col)
    raise AssertionError('degree bound')
def expectmp(A,p): assert s.expand(mp(A)-p)==0 and pmat(p,A)==s.zeros(A.rows)
N=J(2,0); assert N*s.eye(2)[:,1]==s.eye(2)[:,0] and N**2==s.zeros(2)
A=s.Matrix([[1,1,1],[0,1,1],[0,0,3]])
N=A-s.eye(3)
assert N**2==s.Matrix([[0,0,3],[0,0,2],[0,0,4]])
assert N**3==s.Matrix([[0,0,6],[0,0,4],[0,0,8]])
assert N.nullspace()==[s.Matrix([1,0,0])]
assert (N**2).nullspace()==[s.Matrix([1,0,0]),s.Matrix([0,1,0])]==(N**3).nullspace()
T=s.Matrix([[0,4,0],[0,0,0],[0,0,5]])
assert T**3==s.diag(0,0,125)
assert T.nullspace()==[s.Matrix([1,0,0])]
assert (T**3).nullspace()==[s.Matrix([1,0,0]),s.Matrix([0,1,0])]
assert ((T-5*s.eye(3))**3).nullspace()==[s.Matrix([0,0,1])]
N=s.Matrix([[0,0,0,0],[0,0,0,0],[1,0,0,0],[0,1,0,0]])
assert N!=s.zeros(4) and N**2==s.zeros(4)
B=s.Matrix([[-3,9,0],[-7,9,6],[4,0,-6]])
assert B**2==s.Matrix([[-54,54,54],[-18,18,18],[-36,36,36]])
assert B**3==s.zeros(3)
for n in range(9):
    D=s.zeros(n+1)
    for j in range(1,n+1): D[j-1,j]=j
    S=s.diag(*[1/s.factorial(j) for j in range(n+1)])
    assert D*S==S*J(n+1,0)
    expectmp(D,x**(n+1))
T=s.zeros(4)
for j in range(3): T[j+1,j]=1
S=s.Matrix.hstack(*[T**k*s.eye(4)[:,0] for k in [3,2,1,0]])
assert T*S==S*J(4,0)
T=s.zeros(6); T[1,0]=T[2,1]=T[4,3]=1
S=s.eye(6)[:,[2,1,0,4,3,5]]
assert T*S==S*s.diag(J(3,0),J(2,0),J(1,0))
assert nulls(s.diag(J(2,0),J(2,0)),range(5))==[0,2,4,4,4]
assert nulls(J(4,0),range(5))==[0,1,2,3,4]
A=s.Matrix([[6,3,4],[0,6,2],[0,0,7]])
S=s.Matrix([[1,0,10],[0,1,2],[0,0,1]])
assert A*S==S*s.Matrix([[6,3,0],[0,6,0],[0,0,7]])
assert ((A-6*s.eye(3))**3).nullspace()==[s.Matrix([1,0,0]),s.Matrix([0,1,0])]
assert ((A-7*s.eye(3))**3).nullspace()==[s.Matrix([10,2,1])]
expectmp(A,(x-6)**2*(x-7))
A=s.diag(s.Matrix([[4]]),s.Matrix([[2,-3],[0,2]]),s.Matrix([[1,7],[0,1]]))
assert s.expand(A.charpoly(x).as_expr()-(x-4)*(x-2)**2*(x-1)**2)==0
A=s.Matrix([[1,2,3],[0,1,2],[0,0,1]]); N=A-s.eye(3)
assert N**2==s.Matrix([[0,0,4],[0,0,0],[0,0,0]]) and N**3==s.zeros(3)
assert nulls(N,range(4))==[0,1,2,3]
S=s.Matrix([[4,3,0],[0,2,0],[0,0,1]])
assert A*S==S*J(3,1)
A=s.diag(J(2,1),J(2,1),J(3,2),J(1,2))
assert nulls(A-s.eye(8),range(4))==[0,2,4,4]
assert nulls(A-2*s.eye(8),range(5))==[0,2,3,4,4]
expectmp(A,(x-1)**2*(x-2)**3)
for A,r in [(s.Matrix([[3,-1,-1],[2,0,-1],[2,-1,0]]),1),(s.Matrix([[3,-2,0],[1,1,-1],[0,2,-1]]),2)]:
    N=A-s.eye(3); assert N.rank()==r and N**3==s.zeros(3)
    assert (N**2==s.zeros(3))==(r==1)
for r in range(1,6):
    for l in [0,1,2,s.I]:
        N=J(r,0)
        for k in range(9):
            rhs=sum((s.binomial(k,j)*l**(k-j)*N**j for j in range(min(k,r-1)+1)),s.zeros(r))
            assert J(r,l)**k==rhs
assert J(3,1)**100==s.Matrix([[1,100,4950],[0,1,100],[0,0,1]])
coeff=[s.Integer(1)]
for k in range(1,8): coeff.append((s.Integer(1) if k==1 else s.Integer(0))/2-sum((coeff[j]*coeff[k-j] for j in range(1,k)),s.Integer(0))/2)
assert coeff[1:4]==[s.Rational(1,2),-s.Rational(1,8),s.Rational(1,16)]
for r in range(1,8):
    N=J(r,0); R=sum((coeff[j]*N**j for j in range(r)),s.zeros(r))
    assert R**2==s.eye(r)+N
R=s.Matrix([[1,s.Rational(1,2),-s.Rational(1,8)],[0,1,s.Rational(1,2)],[0,0,1]])
assert R**2==J(3,1)
# All numerical HW8 answers, including optional problems.
A=s.diag(J(3,2),J(1,-1),J(1,-1)); expectmp(A,(x-2)**3*(x+1))
B=s.diag(J(2,2),J(1,2),J(1,-1),J(1,-1)); expectmp(B,(x-2)**2*(x+1))
assert [(5-(M-2*s.eye(5)).rank(),5-(M+s.eye(5)).rank()) for M in [A,B]]==[(1,2),(2,2)]
assert nulls(J(3,0),range(4))==[0,1,2,3]
assert nulls(s.diag(J(3,0),J(2,0)),range(5))==[0,2,4,5,5]
A=s.diag(J(2,1),J(3,2),J(1,2))
assert nulls(A-s.eye(6),range(4))==[0,1,2,2]
assert nulls(A-2*s.eye(6),range(5))==[0,2,3,4,4]
A=s.diag(J(3,4),J(2,4),J(1,-1)); expectmp(A,(x-4)**3*(x+1))
assert s.expand(A.charpoly(x).as_expr()-(x-4)**5*(x+1))==0
assert (6-(A-4*s.eye(6)).rank(),6-(A+s.eye(6)).rank())==(2,1)
A=s.Matrix([[3,1,1],[0,3,-1],[0,0,1]])
assert (A-3*s.eye(3)).nullspace()==[s.Matrix([1,0,0])]
assert (A-s.eye(3))*s.Matrix([-3,2,4])==s.zeros(3,1)
assert (A-3*s.eye(3))*(A-s.eye(3))==s.Matrix([[0,2,-1],[0,0,0],[0,0,0]])
expectmp(A,(x-3)**2*(x-1))
print('Week 8 exact source matrices, kernels, Jordan bases, block counts, powers, square roots, and all HW/exam answers passed.')
