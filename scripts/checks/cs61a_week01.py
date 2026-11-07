"""Execute the exact Python listings and verify Week1 examples and algorithms.

Incomplete assignment stubs are compiled, not called. Expected errors in the
text are tested separately. Search checks the worksheet's distinct-input rule.
"""
from pathlib import Path
import ast
import builtins
import contextlib
import doctest
import io
import itertools
import math
import re
import runpy
import sys

ROOT = Path(__file__).resolve().parents[2]
WEEK = ROOT / 'semesters/2026-fall/cs61a/handouts/2026-08-24-functions'
listings = {}
for filename in ['handout.tex', 'solutions.tex']:
    txt = (WEEK / filename).read_text()
    for name, code in re.findall(r'\\begin\{lstlisting\}\[name=([^\]]+)\]\n(.*?)\\end\{lstlisting\}', txt, re.S):
        assert name not in listings
        listings[name] = code
expected = {'squares','local','conflict','noisy','small','abs_stub','two_stub',
            'exam','lab_solution','abs_solution','two_solution','factor_solution','hail_solution'}
assert listings.keys() == expected
spaces = {}
outputs = {}
for name, code in listings.items():
    ns = {}
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        exec(compile(code, name, 'exec'), ns)
    spaces[name] = ns
    outputs[name] = output.getvalue()
assert spaces['local']['first'] == 5
assert spaces['local']['second'] == 16
assert spaces['local']['third'] == 7
assert spaces['local']['x'] == 2 and spaces['local']['y'] == 3
assert spaces['conflict']['answer'] == 9
assert spaces['noisy']['result'] == 8
assert outputs['noisy'] == 'NOISY 2\nNOISY 3\nNOISY 7\n'
assert spaces['noisy']['triple'](4) == 12
assert outputs['exam'] == '-7\nNone\n'
assert spaces['exam']['about'] == 6 and spaces['exam']['face'] == -7
assert spaces['lab_solution']['twenty_twenty_six']() == 2026
square = spaces['squares']['square']
sumsq = spaces['squares']['sum_squares']
assert [square(21), square(2+5), square(square(3)), square(-2)] == [441,49,81,4]
assert sumsq(3,4) == 25 and sumsq(5,12) == 169
for args in [(),(2,3)]:
    try: square(*args)
    except TypeError: pass
    else: raise AssertionError('Expected signature TypeError')
assert [(v,square(v)) for v in [5,12]] == [(5,25),(12,144)]
# Actual required starter doctests, run against the printed solutions.
namespace = {}
for name in ['abs_solution','two_solution','factor_solution','hail_solution']:
    exec(listings[name], namespace)
source = ROOT / 'semesters/2026-fall/cs61a/materials/starter-code/hw01/hw01.py'
starter_ast = ast.parse(source.read_text())
runner = doctest.DocTestRunner()
parser = doctest.DocTestParser()
for func in starter_ast.body:
    if isinstance(func, ast.FunctionDef):
        runner.run(parser.get_doctest(ast.get_docstring(func) or '', namespace,
                                     func.name, str(source), func.lineno))
res = runner.summarize()
assert res.failed == 0 and res.attempted == 15, res
# The two actual source syntax restrictions.
abs_ast = ast.parse(listings['abs_solution']).body[1]
assert isinstance(abs_ast.body[-1],ast.Return)
assert ast.unparse(abs_ast.body[-1]) == 'return f(a, b)'
assert [type(t).__name__ for t in ast.parse(listings['two_solution']).body[0].body] == ['Return']
# Only the two allowed assignments differ from the supplied Q1 body.
original = next(f for f in starter_ast.body if isinstance(f,ast.FunctionDef) and f.name=='a_plus_abs_b')
for node in [original.body[-2].body[0], original.body[-2].orelse[0]]:
    node.value = ast.Name(id='sub' if node is original.body[-2].body[0] else 'add', ctx=ast.Load())
original.body = original.body[1:]  # Docstring is deliberately omitted in printout.
assert ast.dump(original, include_attributes=False) == ast.dump(abs_ast,include_attributes=False)
# Boundary and range properties beyond supplied examples.
for a,b in itertools.product(range(-10,11),repeat=2):
    assert namespace['a_plus_abs_b'](a,b) == a + abs(b)
for args in itertools.product(range(1,10),repeat=3):
    assert namespace['two_of_three'](*args) == sum(x*x for x in sorted(args)[:2])
assert namespace['two_of_three'](1.0,2.0,1e20) == 5.0
assert 1.0**2+2.0**2+1e20**2-max(1.0,2.0,1e20)**2 == 0.0
for n in range(2,301):
    want = max(q for q in range(1,n) if n%q==0)
    assert namespace['largest_factor'](n) == want
for n,want_len,want_max in [(1,1,1),(10,7,16),(27,112,9232)]:
    out=io.StringIO()
    with contextlib.redirect_stdout(out): result=namespace['hailstone'](n)
    vals = list(map(int,out.getvalue().splitlines()))
    assert result == len(vals) == want_len and max(vals) == want_max
    assert vals[0] == n and vals[-1] == 1
    for a,b in zip(vals,vals[1:]): assert b == (a//2 if a%2==0 else 3*a+1)
# All CP1.2--1.3 numeric expressions printed in the packet.
from operator import add,sub,mul,truediv,floordiv
checks = [
 ('42',42),('-1 - -1',0),
 ('1/2+1/4+1/8+1/16+1/32+1/64+1/128',.9921875),
 ('max(7.5,9.5)',9.5),('max(1,-2,3,-4)',3),
 ('pow(100,2)',10000),('pow(2,100)',1267650600228229401496703205376),
 ('max(min(1,-2),min(pow(3,5),-4))',-2),('math.sqrt(256)',16.0),
 ('add(14,28)',42),('sub(100,mul(7,add(8,4)))',16),
 ('2+3*4+5',19),('(2+3)*(4+5)',45),('5/4',1.25),('8/4',2.0),
 ('5//4',1),('-5//4',-2),('truediv(5,4)',1.25),('floordiv(5,4)',1),
 ('mul(add(4,mul(4,6)),add(3,5))',224),
 ('mul(add(2,mul(4,6)),add(3,5))',208),('abs(-2)',2),
 ('2000',2000),('2000+26',2026),('45**2+1',2026),
]
for expr,want in checks: assert eval(expr) == want,(expr,want)
assert round(math.pi*100,7)==314.1592654
assert round(20*math.pi,7)==62.8318531
assert round(121*math.pi,7)==380.1327111
assert round(math.pi*71/223,7)==1.0002380
assert round(2*math.pi,7)==6.2831853
# Names / rebinding / local arithmetic not given as multi-line listings.
ns={};exec('x=2\ny=x+1\nx=5',ns);assert ns['x']==5 and ns['y']==3
exec('x,y=3,4.5\ny,x=x,y',ns);assert ns['x']==4.5 and ns['y']==3
for code,expr,want in [
 ('f=max','f(2,3,4)',4),('f=max\nf=2','f',2),
 ('f=max\nmax=3','f(2,3,4)',4),('max=pow','max(2,5+5)',1024),
 ('max=pow\npow=max','pow(2,10)',1024),('x=2\nx=x+1','x',3),
 ('def g():\n return 1\ng=2\ndef g(h,i):\n return h+i','g(1,2)',3)]:
 ns={};exec(code,ns);assert eval(expr,ns)==want
for code in ['max=5\nmax(1,2)','max=3\nmax(1,2)']:
 try: exec(code,{})
 except TypeError: pass
 else: raise AssertionError('Expected TypeError')
for code in ['1+2=x','x-1=2']:
 try: compile(code,'invalid-target','exec')
 except SyntaxError: pass
 else: raise AssertionError('Expected SyntaxError')
# Printing: exact output AND return values, including deliberate failure.
for expr,wantout,wantresult in [
 ('print(1,2,3)','1 2 3\n',None),
 ('print(print(1),print(2))','1\n2\nNone None\n',None)]:
 out=io.StringIO()
 with contextlib.redirect_stdout(out): value=eval(expr)
 assert out.getvalue()==wantout and value is wantresult
ns={};out=io.StringIO()
with contextlib.redirect_stdout(out): exec('y=print(-3)\nprint(y)',ns)
assert out.getvalue()=='-3\nNone\n' and ns['y'] is None
out=io.StringIO()
with contextlib.redirect_stdout(out):
 try: eval('print(-3)*2')
 except TypeError: pass
 else: raise AssertionError('Expected TypeError')
assert out.getvalue()=='-3\n'
ns={'mul':mul};exec('def square(x):\n mul(x,x)',ns)
assert ns['square'](3) is None
# Floating-point algebra counterexample justifies the packet's qualification.
x=1e-16
assert mul(x,x) != mul(x,x-1)+x
# Actual lecture file (14 doctests), no edits to materials.
lec = ROOT / 'semesters/2026-fall/cs61a/materials/sources/cs61a.org/fa26/assets/lec/02.py'
lecture = runpy.run_path(str(lec))
for name in ['ex','noisy']:
    runner.run(parser.get_doctest(lecture[name].__doc__,lecture,name,str(lec),0))
assert runner.summarize().failed == 0
# Independent exact-call-count search. Every intermediate result is >=5 and
# strictly larger than its operands, so restricting values to target is sound.
small = spaces['small'];f,g,h=[small[n] for n in ['f','g','h']]
assert h(789,12)==78912 and h(12,789)==12789
assert h(f(g(5)),f(f(5)))==107
expr='f(g(h(f(g(5)),g(f(f(5))))))'
assert eval(expr,small)==2026
assert len(expr)==27
assert sum(isinstance(n,ast.Call) for n in ast.walk(ast.parse(expr)))==8
levels=[{5:'5'}]
for calls in range(1,9):
    current={}
    for v,e in levels[calls-1].items():
        for name,op in [('f',f),('g',g)]:
            w=op(v)
            if w<=2026: current.setdefault(w,f'{name}({e})')
    for k in range(calls):
        for a,ae in levels[k].items():
            for b,be in levels[calls-k-1].items():
                if a==b: continue
                w=h(a,b)
                if w<=2026: current.setdefault(w,f'h({ae},{be})')
    levels.append(current)
assert all(2026 not in lev for lev in levels[:8])
assert 2026 in levels[8]
v = 5
for _ in range(8): v = g(v)
assert v == 1025
print('PASS: 13 printed listings, 15 official HW doctests, 14 lecture doctests;')
print('all printed arithmetic/WWPD; factor range, duplicate-input cases, hailstone traces;')
print('worksheet-constrained search: no solution with <=7 calls, 8 calls attain 2026.')
print('Distinct values <=2026 by call count:',[len(lev) for lev in levels])
