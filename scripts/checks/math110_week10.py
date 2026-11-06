"""Exact Week 10 orthogonality, projection, Riesz, least-squares and HW checks."""
import sympy as s
x = s.symbols('x', real=True)
R = s.Rational
ip = lambda u, v: (s.Matrix(u).T * s.conjugate(s.Matrix(v)))[0]
sq = lambda u: s.simplify(ip(u,u))
integ = lambda f,a=-1,b=1: s.integrate(s.expand(f),(x,a,b))
polyip = lambda p,q,a=-1,b=1: s.simplify(integ(p*s.conjugate(q),a,b))
zero = lambda M: M.applyfunc(s.simplify)==s.zeros(*M.shape)
E=s.Matrix.hstack(s.Matrix([1,1,1])/s.sqrt(3),s.Matrix([-1,1,0])/s.sqrt(2),s.Matrix([1,1,-2])/s.sqrt(6))
assert zero(E.T*E-s.eye(3))
E=s.Matrix([[1,1,1,-1],[1,1,-1,1],[1,-1,-1,-1],[1,-1,1,1]])/2
v=s.Matrix([1,2,4,7]);assert E.T*E==s.eye(4)
assert E.T*v==s.Matrix([7,-4,1,2]) and sq(v)==70
for k in range(1,4):
    assert integ(s.cos(k*x),-s.pi,s.pi)==integ(s.sin(k*x),-s.pi,s.pi)==0
    for j in range(1,4):
        assert s.simplify(integ(s.cos(k*x)*s.cos(j*x),-s.pi,s.pi)-s.pi*int(k==j))==0
        assert s.simplify(integ(s.sin(k*x)*s.sin(j*x),-s.pi,s.pi)-s.pi*int(k==j))==0
        assert integ(s.sin(k*x)*s.cos(j*x),-s.pi,s.pi)==0
assert integ(x,0,1)==R(1,2)
for n in [-3,-2,-1,1,2,3]:
    assert s.simplify(s.integrate(x*s.exp(-2*s.pi*s.I*n*x),(x,0,1))+1/(2*s.pi*s.I*n))==0
n=s.symbols('n',integer=True,positive=True)
assert s.summation(1/n**2,(n,1,s.oo))==s.pi**2/6
# Both polynomial Gram--Schmidt calculations, all coefficients and norms.
shift=[s.Integer(1),s.sqrt(3)*(2*x-1),s.sqrt(5)*(6*x*x-6*x+1)]
assert s.Matrix(3,3,lambda i,j:polyip(shift[i],shift[j],0,1))==s.eye(3)
assert polyip(x*x,shift[0],0,1)==R(1,3)
assert polyip(x*x,shift[1],0,1)==s.sqrt(3)/6
assert polyip(x-R(1,2),x-R(1,2),0,1)==R(1,12)
assert polyip(x*x-x+R(1,6),x*x-x+R(1,6),0,1)==R(1,180)
u=[s.Integer(1),x,x*x-R(1,3)]
assert [polyip(t,t) for t in u]==[2,R(2,3),R(8,45)]
e=[1/s.sqrt(2),s.sqrt(R(3,2))*x,s.sqrt(R(5,8))*(3*x*x-1)]
assert s.Matrix(3,3,lambda i,j:polyip(e[i],e[j]))==s.eye(3)
assert ip([1],[s.I])==-s.I
assert ip([s.I,2,3],[2,-5,1])==2*s.I-7
assert ip([s.I,2,3],[-s.I,0,0])==-1
# Riesz representatives: all monomial tests, P2 and P5.
r2=15*(1-3*x*x)/(2*s.pi**2)
r5=105*(27-2*s.pi**2)/(8*s.pi**4)+315*(4*s.pi**2-45)*x*x/(4*s.pi**4)+1575*(21-2*s.pi**2)*x**4/(8*s.pi**4)
for degree,rep in [(2,r2),(5,r5)]:
    for j in range(degree+1):
        assert s.simplify(polyip(x**j,rep)-s.integrate(x**j*s.cos(s.pi*x),(x,-1,1)))==0
assert ip([1,2],[2,-1])==0 and sq([2,-1])==5
# Complement equations and all displayed numeric counterexamples.
assert s.Matrix([[2,3,5]]).rank()==1
assert s.Matrix([[1,0,0,0,0],[0,1,0,0,0]]).nullspace()==[s.eye(5)[:,i] for i in [2,3,4]]
P=s.Matrix([[0,0],[0,1]]);N=s.Matrix([[0,1],[0,0]])
assert P*P==P and N*N==s.zeros(2) and N!=s.zeros(2)
proj=R(9,10)*x-R(1,5)
assert [polyip(x**3,t,0,1) for t in shift[:2]]==[R(1,4),3*s.sqrt(3)/20]
assert [polyip(x**3-proj,t,0,1) for t in [1,x]]==[0,0]
G=s.Matrix([[1,R(1,2)],[R(1,2),R(1,3)]]);b=s.Matrix([R(1,4),R(1,5)])
assert G.inv()*b==s.Matrix([-R(1,5),R(9,10)])
oblique=s.Matrix([[1,1],[0,0]])
assert oblique**2==oblique and sq(oblique*s.Matrix([1,1]))==4 and sq([1,1])==2
assert ip([1,1],[2,0])*s.Matrix([2,0])==s.Matrix([4,0])
# Exact sine approximation system and both reported squared errors.
p=s.pi
powers=[1,3,5]
G=s.Matrix(3,3,lambda i,j:2*p**(powers[i]+powers[j]+1)/(powers[i]+powers[j]+1))
b=s.Matrix([2*p,2*p*(p*p-6),2*p*(p**4-20*p*p+120)])
c=s.Matrix([105*(p**4-153*p*p+1485)/(8*p**6),-315*(p**4-125*p*p+1155)/(4*p**8),693*(p**4-105*p*p+945)/(8*p**10)])
assert zero(G*c-b)
for j,r in enumerate(powers):
    assert s.simplify(s.integrate(x**r*s.sin(x),(x,-p,p))-b[j])==0
best=sum(c[j]*x**powers[j] for j in range(3));tc=s.Matrix([1,-R(1,6),R(1,120)])
err=s.simplify(p-(b.T*c)[0]);terr=s.simplify(p-2*(b.T*tc)[0]+(tc.T*G*tc)[0])
assert abs(float(err)-.000116169)<1e-9 and abs(float(terr)-.118702)<1e-6
assert abs(float(abs(best.subs(x,3)-s.sin(3)))-.001416)<1e-6
assert abs(float(abs(3-R(27,6)+R(243,120)-s.sin(3)))-.383880)<1e-6
for exact,decimal in zip(c,[.987862136,-.155271411,.005643118]):assert abs(float(exact)-decimal)<5e-10
# Pseudoinverse, all image/kernel equations and the least-norm sample.
T=s.Matrix([[1,1,1,0],[0,0,2,1],[0,0,0,0]])
D=s.Matrix([[5,-2,0],[5,-2,0],[1,4,0],[-2,3,0]])/11
K=s.Matrix.hstack(s.Matrix([-1,1,0,0]),s.Matrix([-1,0,1,-2]))
assert T*K==s.zeros(3,2) and K.rank()==2 and T.rank()==2
assert T*D==s.diag(1,1,0) and K.T*D==s.zeros(2,3)
assert (D*T)**2==D*T and (D*T).T==D*T
sample=D*s.Matrix([1,2,3]);assert sample==s.Matrix([1,1,9,4])/11
assert T*sample==s.Matrix([1,2,0]) and sq(T*sample-s.Matrix([1,2,3]))==9
# All numerical homework and real textbook practice answers.
W=s.Matrix.hstack(s.Matrix([1,-1,1,0]),s.Matrix([0,2,1,0]))
C=s.Matrix.hstack(s.Matrix([3,1,-2,0]),s.Matrix([0,0,0,1]))
assert W.T*C==s.zeros(2) and W.rank()==C.rank()==2
assert [polyip(t,x+1) for t in [x-R(1,3),x*x-R(1,3)]]==[0,0]
for f in [s.Integer(1),x]:assert polyip(f,1+3*x)==s.integrate(f,(x,0,2))
aw=s.Matrix([1,3]);av=s.Matrix([1,2]);pu=R(7,10)*aw;pv=av-pu
assert pu==s.Matrix([R(7,10),R(21,10)]) and pv==s.Matrix([R(3,10),-R(1,10)])
assert ip(pv,aw)==0
# Complex scalar choice used in HW10 and Exercise6: symbolic first-slot-linear check.
a,b,c,d,e0,f,g,h=s.symbols('a b c d e f g h',real=True)
u=s.Matrix([a+s.I*b,c+s.I*d]);w=s.Matrix([e0+s.I*f,g+s.I*h])
mixed=s.expand(ip(u,w));den=sq(w);t=-mixed/den
assert s.simplify(sq(u+t*w)-sq(u)+s.expand_complex(mixed*s.conjugate(mixed))/den)==0
print('Week 10 exact checks passed: ON/GS, Fourier, Riesz, complements, projections, sine approximation, pseudoinverse, all HW/practice computations.')
