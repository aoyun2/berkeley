"""Execute the Week3 printed code, original public examples and independent checks."""
from pathlib import Path
from html.parser import HTMLParser
import ast
import contextlib
import doctest
import importlib.util
import io
import math
import re
import runpy
import tempfile

ROOT = Path(__file__).resolve().parents[2]
W = ROOT / 'semesters/2026-fall/cs61a/handouts/2026-09-07-functional-abstraction'
MAT = ROOT / 'semesters/2026-fall/cs61a/materials'

def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def capture(call, *args):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        result = call(*args)
    return result, out.getvalue()

regions = {}
for path in W.glob('*.py'):
    lines = path.read_text().splitlines()
    for i, line in enumerate(lines):
        match = re.fullmatch(r'# BEGIN (\w+)', line)
        if match:
            label = match.group(1)
            end = lines.index('# END ' + label, i + 1)
            assert label not in regions
            regions[label] = (path.name, i+2, end)
ranges = (W/'code-ranges.tex').read_text()
for name, (filename, start, end) in regions.items():
    exact = (r'\expandafter\def\csname code' + name + r'\endcsname{\lstinputlisting[firstline='
             + str(start) + ',lastline=' + str(end) + ']{' + filename + '}}')
    assert exact in ranges, (name, 'stale code range')
combined = ' '.join((W/f).read_text() for f in ['handout.tex', 'problems.tex', 'solutions.tex'])
used = {s.split('}', 1)[0] for s in combined.split(chr(92)+'codeblock{')[1:]}
assert used == regions.keys(), (used-regions.keys(), regions.keys()-used)

ex = load(W/'examples.py', 'week3_examples')
lab = load(W/'lab_solutions.py', 'week3_lab')
disc = load(W/'discussion_solutions.py', 'week3_disc')
exam = load(W/'exam_solutions.py', 'week3_exam')
assert ex.summation(5, lambda x: x) == 15
assert ex.summation(5, lambda x: (1/2)**x) == 31/32
assert ex.summation(5, lambda x: x**3) == 225
assert ex.summation(5, lambda k: 8/(4*k-3)/(4*k-1)) == 3.041839618929402
assert ex.summation(5, ex.term) == 0.4979423868312757
assert math.isclose(ex.summation(5, lambda k: (1/5)**k), 781/3125)
assert ex.curry(pow)(3)(2) == 9
assert ex.curry(pow)(1/2)(5) == 1/32
assert ex.summation(5, ex.curry(pow)(3)) == 363
assert ex.twice(ex.square)(3) == 81
assert (lambda f: lambda x: f(f(x)))(lambda y: y*y)(3) == 81
assert (lambda x: 2*(lambda x: 3)(4)*x)(5) == 30
assert (1 if True else 1/0) == 1
scale = lambda f, x, k: k*f(x)
assert [scale(ex.square, 3, 2), scale(ex.square, 2, 5), scale(lambda x:x+10,5,2)] == [18,20,30]
ns = {}
assert capture(exec, "bear=-1\noski=lambda print:print(bear)\nbear=-2\nprint(oski(abs))", ns) == (None, '2\n')
assert capture(eval, "bool(print('fool'))") == (False, 'fool\n')
assert [bool(v) for v in [0, -1, 0.0, ' ', '', False]] == [False,True,False,True,False,False]

# Execute the original buggy loop in a fresh namespace and check its exact failure.
bug = (W/'max_bug.txt').read_text()
ns = {}
try:
    exec(bug, ns)
    raise AssertionError('expected shadowed max TypeError')
except TypeError as error:
    assert 'not callable' in str(error)
assert ns['max'] == 1 and ns['y'] == 2
ns = {}
exec(bug.replace('max = y', 'largest = y'), ns)
assert ns['largest'] == 9 and ns['y'] == 10

assert lab.n == 7 and lab.g == 15 and lab.f() == 15
assert disc.team is abs and disc.t is abs and disc.work == 3
assert disc.which()() == 3 and disc.one == 1
assert capture(disc.make_keeper(5), lambda x:x%2==0) == (None, '2\n4\n')
assert capture(disc.make_keeper(5), lambda x:True) == (None, '1\n2\n3\n4\n5\n')
assert capture(disc.make_keeper(5), lambda x:False) == (None, '')
assert [disc.find_digit(k)(x) for k,x in [(2,3456),(2,5678),(1,10),(4,789)]] == [5,7,0,0]
assert [disc.match_k(k)(x) for k,x in [(2,1010),(2,2010),(1,1010),(1,1),(1,2111111111111111),(3,123123),(2,123123)]] == [True,False,False,True,False,True,False]
assert disc.every(lambda d:d%2==1)(37511) and not disc.every(lambda d:d%2==1)(2023)
assert disc.count_if(lambda d:d==3)(431663334231) == 5
assert disc.count_at_least(3)(431663334231) == 9
assert lab.piecewise(lambda x:-x, lambda x:x, 0)(-1) == 1
# The unselected branch must not run, including at the boundary.
def forbidden(x):
    raise AssertionError('unselected branch was called')
assert lab.piecewise(forbidden, lambda x:x, 0)(0) == 0
assert lab.piecewise(lambda x:-x, forbidden, 0)(-2) == 2

# Independent finite-domain oracles, not copies of the printed arithmetic scans.
for x in range(1, 5000):
    digits = list(map(int, str(x)))
    for k in range(1, 7):
        assert disc.find_digit(k)(x) == (digits[-k] if k <= len(digits) else 0)
        assert disc.match_k(k)(x) == all(a==b for a,b in zip(digits, digits[k:]))
    for threshold in [1,3,5,10]:
        predicate = lambda d: d >= threshold
        assert disc.every(predicate)(x) == all(predicate(d) for d in digits)
        assert disc.count_if(predicate)(x) == sum(predicate(d) for d in digits)
        assert disc.count_at_least(threshold)(x) == sum(d>=threshold for d in digits)

def prime_reference(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n)+1))
for n in range(6, 300):
    candidates = [p for p in range(2,2*n) if prime_reference(p)]
    assert ex.nearest_prime(n) == min(candidates, key=lambda p:(abs(p-n),-p))
for n in range(0, 101):
    assert lab.count_cond(lambda n,i:i*i<=n)(n) == math.isqrt(n)
    calls = []
    def pred(a, i):
        calls.append((a,i))
        return i % 2 == 0
    assert lab.count_cond(pred)(n) == n//2
    assert calls == [(n,i) for i in range(1,n+1)]
functions = [lambda x:x+1, lambda x:x*2, lambda x:x+3]
cyclic = lab.cycle(*functions)
for n in range(20):
    for start in range(-3,4):
        result = start
        for i in range(n):
            result = functions[i%3](result)
        assert cyclic(n)(start) == result
        assert cyclic(n)(start) == result  # Fresh local progress on reuse.
for n,x,want in [(0,5,5),(2,1,4),(3,2,9),(4,2,10),(6,1,19)]:
    assert cyclic(n)(x) == want

assert exam.funsquare_D(lambda x:3*x)(5) == exam.funsquare_F(lambda x:3*x)(5) == 45
for function,args in [(exam.funsquare_A,(lambda x:3*x,)),
                      (exam.funsquare_C,(lambda x:3*x,)),
                      (exam.funsquare_E,(lambda x:3*x,))]:
    try:
        function(*args)
        raise AssertionError('incorrect funsquare accepted')
    except TypeError:
        pass
try:
    exam.funsquare_B(lambda x:3*x)(5)
    raise AssertionError('zero-argument inner accepted x')
except TypeError:
    pass
ns = {'new_print':exam.new_print}
assert capture(exec, "og=print\nprint=new_print(print)\nprint=new_print(print)\nog('print returned',print(2))",ns) == (None, '2\nWhat?\nprint returned What?\n')
for n in range(2, 25):
    for modulus in range(2, 5):
        use = lambda i: i % modulus != 0
        indices = [i for i in range(1,n+1) if use(i)]
        if len(indices)<2:
            continue
        for term in [lambda x:x*x, lambda x:x%5, lambda x:-x]:
            values = list(map(term, indices))
            expected = max(abs(a-b) for a,b in zip(values, values[1:]))
            assert exam.make_gap(use)(n,term) == expected
assert exam.make_gap(lambda i:i%2==1)(8,lambda x:x%5)==3
# Check restrictions on the actual answer, excluding provided helper f.
node = next(n for n in ast.parse((W/'exam_solutions.py').read_text()).body
            if isinstance(n, ast.FunctionDef) and n.name=='make_gap')
assert not any(isinstance(n,(ast.If,ast.IfExp,ast.For,ast.NamedExpr,ast.List,ast.Subscript,ast.BoolOp)) for n in ast.walk(node))
assert not {'map','filter','range'} & {n.id for n in ast.walk(node) if isinstance(n,ast.Name)}
node = next(n for n in ast.parse((W/'discussion_solutions.py').read_text()).body
            if isinstance(n,ast.FunctionDef) and n.name=='find_digit')
assert len(node.body)==2 and isinstance(node.body[1],ast.Return) and isinstance(node.body[1].value,ast.Lambda)
assert not any(isinstance(n,ast.Subscript) for n in ast.walk(node))

# Original source examples, preserving authentic docstrings in filled scratch modules.
runner = doctest.DocTestRunner(optionflags=doctest.ELLIPSIS)
parser = doctest.DocTestParser()
failures = io.StringIO()
official = ast.parse((MAT/'starter-code/lab02/lab02.py').read_text())
solutions = {n.name:n for n in ast.parse((W/'lab_solutions.py').read_text()).body if isinstance(n,ast.FunctionDef)}
for node in official.body:
    if isinstance(node,ast.FunctionDef) and node.name in solutions:
        doc = node.body[:1] if ast.get_docstring(node) else []
        node.body = doc + solutions[node.name].body
with tempfile.TemporaryDirectory(prefix='cs61a-week03-') as temporary:
    filled = Path(temporary)/'lab02.py'
    filled.write_text(ast.unparse(ast.fix_missing_locations(official)))
    mod = load(filled, 'filled_lab2')
    for node in official.body:
        if isinstance(node,ast.FunctionDef) and node.name in solutions:
            doc = ast.get_docstring(node)
            runner.run(parser.get_doctest(doc,mod.__dict__,node.name,str(filled),0),out=failures.write)

class PreBlocks(HTMLParser):
    def __init__(self):
        super().__init__();self.active=False;self.parts=[];self.blocks=[]
    def handle_starttag(self,tag,attrs):
        if tag=='pre':self.active=True;self.parts=[]
    def handle_data(self,data):
        if self.active:self.parts.append(data)
    def handle_endtag(self,tag):
        if tag=='pre' and self.active:
            self.blocks.append(''.join(self.parts));self.active=False
pre = PreBlocks()
pre.feed((MAT/'sources/cs61a.org/fa26/discussions/disc02/index.html').read_text())
for block in pre.blocks:
    if '>>>' not in block:
        continue
    tree = ast.parse(block)
    for node in tree.body:
        if isinstance(node,ast.FunctionDef):
            doc = ast.get_docstring(node)
            if doc and '>>>' in doc:
                runner.run(parser.get_doctest(doc,disc.__dict__,node.name,'disc02.html',0),out=failures.write)

# Locked WWPD inputs are executed; no hash guessing or invented unlocked source.
expected = {
    'short_circuit':['13\n','0\n','False\n','True\n','ERROR','True\n','True\n','-1\n','1\n',"3\n''\n",'',"'positive'\n","'zero'\n","''\n"],
    'hof_wwpd':['','beets\n','FUNCTION',"sweets\n'cake'\n",'sweets\n',"'cake'\n",'','FUNCTION',"sweets\n'cake'\n",'','30\n'],
    'lambda_wwpd':['FUNCTION','','5\n','3\n','','','FUNCTION','12\n','','','16\n','','','4\n','','11\n','','FUNCTION','1000\n','None\n'],
}
wwpd_count = 0
for stem,wants in expected.items():
    source = (MAT/'starter-code/lab02/tests'/(stem+'.py')).read_text()
    fn = next(n for n in ast.parse(source).body if isinstance(n,ast.FunctionDef))
    doc = ast.get_docstring(fn)
    cases = parser.get_examples(doc)
    assert len(cases)==len(wants),(stem,len(cases),len(wants))
    ns = {}
    for case,want in zip(cases,wants):
        out = io.StringIO()
        try:
            with contextlib.redirect_stdout(out):
                exec(compile(case.source,stem,'single'),ns)
            actual = out.getvalue()
            if want=='FUNCTION':
                assert re.fullmatch(r'<function .* at 0x[0-9a-f]+>\n',actual),(case.source,actual)
            else:
                assert actual==want,(case.source,actual,want)
        except ZeroDivisionError:
            assert want=='ERROR'
        wwpd_count += 1
    # The printed problem transcript is a faithful source copy with answer hashes replaced.
    printed = doc.split('\n',1)[1].strip()
    printed = re.sub(r'LOCKED: [a-f0-9]+','______',printed)
    printed = re.sub(r'  # doctest: \+ELLIPSIS','',printed)
    assert (W/(stem+'.txt')).read_text()==printed+'\n'

lecture = MAT/'sources/cs61a.org/fa26/assets/lec/06.py'
values,printed = capture(runpy.run_path,str(lecture))
assert printed=='0.4979423868312757\n363\n'
lecture_runner = doctest.DocTestRunner()
lecture_runner.run(parser.get_doctest(values['summation'].__doc__,values,'L6 summation',str(lecture),0))
assert lecture_runner.summarize().failed==0
result = runner.summarize()
if result.failed:
    print(failures.getvalue())
assert result.failed==0,result
print(f'PASS: {result.attempted} original lab/discussion doctest examples; {wwpd_count} exact WWPD session entries; original L6 code/output/doctest.')
print('PASS: all printed modules/ranges; 29,994 digit-position/pair checks; predicate/cycle/prime oracles; real exam callbacks, output, errors and syntax restrictions.')
