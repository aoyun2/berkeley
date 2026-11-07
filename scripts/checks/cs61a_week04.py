"""Check Week4 printed implementations against real tests and independent oracles."""
from pathlib import Path
from html.parser import HTMLParser
import ast
import contextlib
import doctest
import importlib.util
import io
import itertools
import math
import re
import runpy
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[2]
W=ROOT/'semesters/2026-fall/cs61a/handouts/2026-09-14-recursion'
MAT=ROOT/'semesters/2026-fall/cs61a/materials'

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod

def output(call,*args):
    stream=io.StringIO()
    with contextlib.redirect_stdout(stream):result=call(*args)
    return result,stream.getvalue()

regions={}
for path in W.glob('*.py'):
    lines=path.read_text().splitlines()
    for i,line in enumerate(lines):
        match=re.fullmatch(r'# BEGIN (\w+)',line)
        if match:
            name=match.group(1);end=lines.index('# END '+name,i+1)
            assert name not in regions
            regions[name]=(path.name,i+2,end)
ranges=(W/'code-ranges.tex').read_text()
for name,(filename,start,end) in regions.items():
    exact=(r'\expandafter\def\csname code'+name+r'\endcsname{\lstinputlisting[firstline='
           +str(start)+',lastline='+str(end)+']{'+filename+'}}')
    assert exact in ranges,(name,'stale printed range')
combined=' '.join((W/name).read_text() for name in ['handout.tex','problems.tex','solutions.tex'])
used={part.split('}',1)[0] for part in combined.split(chr(92)+'codeblock{')[1:]}
assert used==regions.keys(),(used-regions.keys(),regions.keys()-used)

ex=load(W/'examples.py','week4examples')
disc=load(W/'discussion_solutions.py','week4discussion')
hw=load(W/'hw_solutions.py','week4homework')
exam=load(W/'exam_solutions.py','week4exam')
assert (lambda f:lambda x:f(f(x)))(lambda y:y*y)(3)==81
assert [ex.square(3),ex.cube(3),ex.reverse(pow)(2,3),ex.curry(pow)(5)(2),ex.exp(3)(2)]==[9,27,9,25,8]
for n,want in [(9,9),(18117,18),(738,18),(9437184,36),(11408855402054064613470328848384,126)]:
    assert ex.sum_digits(n)==want==sum(map(int,str(n)))
for n in range(101):
    assert ex.fact(n)==ex.fact_iter(n)==ex.fact_tail(n)==math.factorial(n)
    assert ex.fact_k(n,10)==10*math.factorial(n)
    assert ex.is_even(n)==(n%2==0) and ex.is_odd(n)==(n%2==1)
assert ex.fact_k(5,1)==120 and ex.fact_k(5,10)==1200 and ex.fact_k(0,10)==10
assert ex.play(lambda n:1,lambda n:1)==1
assert output(ex.play_alice,20)==(None,'Bob wins!\n')
assert output(ex.cascade,2013)==(None,'2013\n201\n20\n2\n20\n201\n2013\n')
assert output(disc.swipe,2837)==(None,'7\n3\n8\n2\n8\n3\n7\n')
assert disc.skip_factorial(5)==15 and disc.skip_factorial(8)==384
assert [disc.is_prime(n) for n in [2,16,521]]==[True,False,True]
assert output(disc.hailstone,10)==(7,'10\n5\n16\n8\n4\n2\n1\n')
assert output(disc.hailstone,1)==(1,'1\n')
assert [ex.unique_prime_factors(n) for n in [72000,51,9,576]]==[3,2,1,2]
for n in range(2,501):
    prime_factors={d for d in range(2,n+1) if n%d==0 and all(d%k for k in range(2,math.isqrt(d)+1))}
    assert ex.unique_prime_factors(n)==len(prime_factors)
    assert disc.is_prime(n)==(prime_factors=={n})
for n in range(1,21):
    assert disc.skip_factorial(n)==math.prod(range(n,0,-2))
    who,direction=0,1
    speakers=[]
    for value in range(1,21):
        speakers.append(who+1)
        if value%7==0 or '7' in str(value):direction=-direction
        who=(who+direction)%n
    assert [disc.sevens(i,n) for i in range(1,21)]==speakers
assert [disc.sevens(i,5) for i in range(1,21)]==[1,2,3,4,5,1,2,1,5,4,3,2,1,5,1,2,3,2,1,5]

# Test that a strategy is called once on each actual Twenty-One turn.
calls=[]
def s0(n):calls.append((0,n));return 2
def s1(n):calls.append((1,n));return 3
assert ex.play(s0,s1,goal=6)==1 and calls==[(0,0),(1,2),(0,5)]

fib_values=[0,1]
for n in range(2,17):fib_values.append(fib_values[-1]+fib_values[-2])
assert [ex.fib(n) for n in range(17)]==fib_values and ex.fib(6)==8
for n,m,want in [(6,4,9),(5,5,7),(10,10,42),(15,15,176),(20,20,627)]:
    counts=[1]+[0]*n
    for part in range(1,m+1):
        for target in range(part,n+1):counts[target]+=counts[target-part]
    assert ex.count_partitions(n,m)==want==counts[n]
actual_partitions={tuple(part for part,c in enumerate(counts,1) for _ in range(c))
                   for counts in itertools.product(range(7),repeat=4)
                   if sum((i+1)*c for i,c in enumerate(counts))==6}
assert actual_partitions=={(2,4),(1,1,4),(3,3),(1,2,3),(1,1,1,3),(2,2,2),(1,1,2,2),(1,1,1,1,2),(1,1,1,1,1,1)}
assert [ex.count_park(n) for n in range(5)]==[1,2,5,12,29]
assert ex.count_park(-1)==0
assert [ex.streak(n) for n in [22222,4,22322,99999,505,707,7070,33333333333333]]==[True,True,False,False,False,False,False,True]

# Virtual square world: code is executed with the actual four-function interface.
for size in range(1,101):
    state=[1,1,0]  # row,column,heading;0east,1north,2west,3south
    def next_position():
        row,col,heading=state
        dr,dc=[(0,1),(1,0),(0,-1),(-1,0)][heading]
        return row+dr,col+dc
    def clear():
        row,col=next_position();return 1<=row<=size and 1<=col<=size
    def move():
        assert clear(),('robot hit wall',size,state)
        state[:2]=next_position()
    def left():state[2]=(state[2]+1)%4
    disc.front_is_clear=clear;disc.front_is_blocked=lambda:not clear()
    disc.move=move;disc.turn_left=left
    disc.main()
    assert state==[1,1+size//2,2],(size,state)

# Independent decimal-string oracles are verification only, not student algorithms.
for n in range(1,3000):
    digits=list(map(int,str(n)))
    assert hw.num_eights(n)==digits.count(8)
    assert hw.digit_distance(n)==sum(abs(a-b) for a,b in zip(digits,digits[1:]))
    assert ex.streak(n)==(len(set(digits))==1 and 1<=digits[0]<=6)
    assert ex.sum_digits(n)==sum(digits)
for n in range(1,1200):
    digits=str(n)
    for t in range(6):
        expected=max([0]+[int(''.join(choice)) for k in range(1,min(t,len(digits))+1)
                          for choice in itertools.combinations(digits,k)])
        assert hw.max_subseq(n,t)==expected
for n in range(1,101):
    for odd,even in [(lambda x:x,lambda x:x*x),(lambda x:x*x,lambda x:x),
                     (lambda x:3*x,lambda x:x*x),(lambda x:x*x,lambda x:3*x)]:
        assert hw.interleaved_sum(n,odd,even)==sum((odd if i%2 else even)(i) for i in range(1,n+1))
for total in [1,5,10,15,20,45,100,200]:
    counts=[1]+[0]*total
    for coin in [1,5,10,25]:
        for amount in range(coin,total+1):counts[amount]+=counts[amount-coin]
    assert hw.count_coins(total)==counts[total]
assert [hw.count_coins(t) for t in [15,10,20,45,100,200]]==[6,4,9,39,242,1463]

# Validate each printed Hanoi move by executing it against three actual stacks.
for count in range(1,7):
    for start,end in itertools.permutations([1,2,3],2):
        result,printed=output(hw.move_stack,count,start,end)
        pegs={i:[] for i in [1,2,3]};pegs[start]=list(range(count,0,-1))
        lines=printed.splitlines()
        for line in lines:
            match=re.fullmatch(r'Move the top disk from rod (\d) to rod (\d)',line)
            assert match,line
            a,b=map(int,match.groups());disk=pegs[a].pop()
            assert not pegs[b] or pegs[b][-1]>disk
            pegs[b].append(disk)
        assert result is None and pegs[end]==list(range(count,0,-1)) and len(lines)==2**count-1
for n in range(15):assert hw.make_anonymous_factorial()(n)==math.factorial(n)

for n in range(10000):
    expected=int(''.join(k for k,_ in itertools.groupby(str(n))))
    assert exam.collapse(n)==expected
for a in range(251):
    for b in range(251):
        digits=iter(str(b) if b else '')
        expected=a==0 or all(any(d==wanted for d in digits) for wanted in str(a))
        assert exam.contains(a,b)==expected,(a,b,expected)
assert exam.contains(0,7) is True
assert [exam.contains(a,b) for a,b in [(357,12345678),(753,12345678),(357,37)]]==[True,False,False]
assert [exam.collapse(n) for n in [1234,12234441,0,3,11200000013333]]==[1234,12341,0,3,12013]
assert [hw.digit_distance(n) for n in [61,71253,6]]==[5,12,0]
for n in [94720,919321,2025,20252025,3456,357,123]:
    for cond in [lambda d:d%2==1,lambda d:d<4,lambda d:True,lambda d:False]:
        prefixes=[int(str(n)[:k]) for k in range(len(str(n)),0,-1)]
        expected=next((p for p in prefixes if all(cond(int(d)) for d in str(p))),0)
        assert exam.prefix_digits(n,cond)==exam.prefix_digits_loop(n,cond)==expected
assert [exam.prefix_digits(n,lambda d:d%2==1) for n in [94720,919321,2025]]==[9,9193,0]
assert exam.prefix_digits(20252025,lambda d:d<4)==202
assert exam.prefix_digits(20252025,lambda d:True)==20252025
assert output(exam.numbered_hailstone,10)==(None,'1 10 -> 5\n2 5 -> 16\n3 16 -> 8\n4 8 -> 4\n5 4 -> 2\n6 2 -> 1\n')

# Actual public syntax checks, including restrictions stronger than brief prose.
tree=ast.parse((W/'hw_solutions.py').read_text())
functions={n.name:n for n in tree.body if isinstance(n,ast.FunctionDef)}
for name in ['num_eights','digit_distance','interleaved_sum','count_coins','max_subseq']:
    assert not any(isinstance(n,(ast.For,ast.While,ast.AsyncFor)) for n in ast.walk(functions[name]))
assert not any(isinstance(n,(ast.Assign,ast.AnnAssign,ast.AugAssign,ast.NamedExpr)) for n in ast.walk(functions['num_eights']))
assert not any(isinstance(n,(ast.Mod,ast.FloorDiv,ast.Mult,ast.BitAnd,ast.BitOr,ast.BitXor)) for n in ast.walk(functions['interleaved_sum']))
assert len(functions['make_anonymous_factorial'].body)==1
assert 'make_anonymous_factorial' not in ast.unparse(functions['make_anonymous_factorial'].body[0])
robot=next(n for n in ast.parse((W/'discussion_solutions.py').read_text()).body if isinstance(n,ast.FunctionDef) and n.name=='main')
assert all(isinstance(n,(ast.If,ast.Expr,ast.Call,ast.Name,ast.Load)) for stmt in robot.body for n in ast.walk(stmt))
for name in ['swipe','is_prime']:
    fn=next(n for n in ast.parse((W/'discussion_solutions.py').read_text()).body if isinstance(n,ast.FunctionDef) and n.name==name)
    assert not any(isinstance(n,(ast.For,ast.While)) for n in ast.walk(fn))
    assert 'str' not in {n.id for n in ast.walk(fn) if isinstance(n,ast.Name)}
contains=next(n for n in ast.parse((W/'exam_solutions.py').read_text()).body if isinstance(n,ast.FunctionDef) and n.name=='contains')
assert not {'str','repr','list','tuple'} & {n.id for n in ast.walk(contains) if isinstance(n,ast.Name)}
assert not any(isinstance(n,(ast.List,ast.Subscript)) for n in ast.walk(contains))

# Retain original signature/docstring and inspect-based tests in a scratch copy.
runner=doctest.DocTestRunner(optionflags=doctest.ELLIPSIS)
parser=doctest.DocTestParser();failures=io.StringIO()
official=ast.parse((MAT/'starter-code/hw03/hw03.py').read_text())
for node in official.body:
    if isinstance(node,ast.FunctionDef) and node.name in functions:
        node.body=(node.body[:1] if ast.get_docstring(node) else [])+functions[node.name].body
with tempfile.TemporaryDirectory(prefix='cs61a-week04-') as temporary:
    filled=Path(temporary)/'hw03.py';filled.write_text(ast.unparse(ast.fix_missing_locations(official)))
    module=load(filled,'filled_hw3')
    for node in official.body:
        if isinstance(node,ast.FunctionDef):
            doc=ast.get_docstring(node)
            if doc and '>>>' in doc:
                runner.run(parser.get_doctest(doc,module.__dict__,node.name,str(filled),0),out=failures.write)

class PreBlocks(HTMLParser):
    def __init__(self):super().__init__();self.active=False;self.parts=[];self.blocks=[]
    def handle_starttag(self,tag,attrs):
        if tag=='pre':self.active=True;self.parts=[]
    def handle_data(self,data):
        if self.active:self.parts.append(data)
    def handle_endtag(self,tag):
        if tag=='pre' and self.active:self.blocks.append(''.join(self.parts));self.active=False
pre=PreBlocks();pre.feed((MAT/'sources/cs61a.org/fa26/discussions/disc03/index.html').read_text())
for block in pre.blocks:
    if '>>>' not in block:continue
    for node in ast.parse(block).body:
        if isinstance(node,ast.FunctionDef):
            doc=ast.get_docstring(node)
            if doc and '>>>' in doc:
                runner.run(parser.get_doctest(doc,disc.__dict__,node.name,'disc03.html',0),out=failures.write)
result=runner.summarize()
if result.failed:print(failures.getvalue())
assert result.failed==0,result

lecture_dir=MAT/'sources/cs61a.org/fa26/assets/lec'
sys.path.insert(0,str(MAT/'starter-code/hog'))  # Authentic supplied ucb.py dependency.
lecture_runner=doctest.DocTestRunner()
for name in ['09.py','10.py']:
    namespace=runpy.run_path(str(lecture_dir/name))
    for key,value in namespace.items():
        if callable(value) and getattr(value,'__doc__',None) and '>>>' in value.__doc__:
            lecture_runner.run(parser.get_doctest(value.__doc__,namespace,key,name,0))
assert lecture_runner.summarize().failed==0
try:
    runpy.run_path(str(lecture_dir/'08.py'))
    raise AssertionError('original L8 placeholder should fail')
except NameError as error:
    assert error.name=='_______________'
source=ast.parse((lecture_dir/'08.py').read_text())
definitions=ast.Module(body=[n for n in source.body if isinstance(n,ast.FunctionDef)],type_ignores=[])
namespace={};exec(compile(definitions,'isolated-original-08.py','exec'),namespace)
for name in ['square','cube']:
    fn=namespace[name]
    lecture_runner.run(parser.get_doctest(fn.__doc__,namespace,name,'08.py definitions only',0))
assert lecture_runner.summarize().failed==0
print(f'PASS: {result.attempted} unmodified HW3/Discussion3 doctest examples; {lecture_runner.summarize().attempted} original lecture examples (L8 definitions explicitly isolated from its unfilled top-level blank).')
print('PASS: every marked printed range/module; original numeric/output examples; digit/subsequence/prime/partition/coin oracles; 100 Karel worlds; legal Hanoi moves; callback counts and syntax restrictions.')
