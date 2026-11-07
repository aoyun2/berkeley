"""Run actual printed Week2 source and the official unmodified tests in scratch.

Filled official modules are made by replacing TODO bodies with study solutions,
retaining official signatures/docstrings. Original materials are never edited.
Locked WWPD questions are executed with explicit expected output separately.
"""
from pathlib import Path
import ast
import contextlib
import doctest
import importlib.util
import io
import itertools
import math
import os
import re
import runpy
import shutil
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[2]
MAT=ROOT/'semesters/2026-fall/cs61a/materials'
W=ROOT/'semesters/2026-fall/cs61a/handouts/2026-08-31-control-higher-order'
# Verify that every printed source range still matches its exact marked region.
region_map={}
for path in W.glob('*.py'):
    lines=path.read_text().splitlines()
    for i,line in enumerate(lines):
        match=re.fullmatch(r'# BEGIN (\w+)',line)
        if match:
            name=match.group(1);end=lines.index('# END '+name,i+1)
            assert name not in region_map
            region_map[name]=(path.name,i+2,end)
range_text=(W/'code-ranges.tex').read_text()
for name,(filename,start,end) in region_map.items():
    exact=r'\expandafter\def\csname code'+name+r'\endcsname{\lstinputlisting[firstline='+str(start)+',lastline='+str(end)+']{'+filename+'}}'
    assert exact in range_text,(name,'stale printed source range')
combined=' '.join((W/f).read_text() for f in ['handout.tex','problems.tex','solutions.tex'])
used={part.split('}',1)[0] for part in combined.split(chr(92)+'codeblock{')[1:]}
assert used==region_map.keys(),(used-region_map.keys(),region_map.keys()-used)
sys.path.insert(0,str(MAT/'starter-code/hog'))

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod
    spec.loader.exec_module(mod)
    return mod

def output(call,*args,**kw):
    out=io.StringIO()
    with contextlib.redirect_stdout(out): value=call(*args,**kw)
    return value,out.getvalue()

ex=load(W/'examples.py','week2examples')
lab=load(W/'lab_solutions.py','week2lab')
disc=load(W/'discussion_solutions.py','week2disc')
hw=load(W/'hw_solutions.py','week2hw')
hog=load(W/'hog_solutions.py','week2hog')
exam=load(W/'exam_solutions.py','week2exam')
stubs=load(W/'exam_stubs.py','week2stubs')  # Define, never call incomplete stubs.
# Every numerical/source example in the handout.
assert output(ex.print_once,2,ex.increment)==(3,'3\n')
assert ex.percent_difference(40,50)==25.0
assert [ex.absolute_value(x) for x in [-2,0,3]]==[2,0,3]
assert [ex.fib(n) for n in [1,3,8,50]]==[1,2,21,12586269025]
i,total=0,0;states=[]
while i<3:i=i+1;total=total+i;states.append((i,total))
assert states==[(1,1),(2,3),(3,6)]
assert output(ex.prime_factors,858)==(None,'2\n3\n11\n13\n')
for n,vals in [(8,[2,2,2]),(9,[3,3]),(10,[2,5]),(11,[11]),(12,[2,2,3]),(1,[])]:
    assert output(ex.prime_factors,n)==(None,''.join(f'{v}\n' for v in vals))
assert ex.pressure(1,273.15)==2269.974834
assert ex.pressure(1,273.15,3*6.022e23)==6809.924502
assert [round(1.23,1),round(1.23,0),round(1.23,5),round(1.23)]==[1.2,1.0,1.23,1]
assert type(round(1.23,0)) is float and type(round(1.23)) is int
for n,f,want in [(3,ex.cube,36),(5,ex.cube,225),(100,ex.identity,5050),
                  (100,ex.cube,25502500),(10,ex.square,385),
                  (100,ex.pi_term,3.1365926848388144),(1000000,ex.pi_term,3.141592153589902)]:
    assert ex.summation(n,f)==want
assert ex.cube(7)==343 and ex.apply_twice(ex.square,2)==16
assert ex.make_adder(3)(4)==7
assert ex.make_adder(5)(4)==9 and ex.make_adder(3)(4)==7
assert ex.compose1(ex.square,ex.increment)(12)==169
assert ex.square_lambda(12)==144
assert ex.compose_lambda(lambda x:x*x,lambda y:y+1)(12)==169
assert ex.curried_pow(2)(3)==8
assert ex.curry2(pow)(2)(5)==ex.uncurry2(ex.curry2(pow))(2,5)==32
assert output(ex.map_to_range,0,10,ex.curried_pow(2))==(None,'1\n2\n4\n8\n16\n32\n64\n128\n256\n512\n')
v,out=output(ex.triple,12)
assert v==36 and re.fullmatch(r'->  <function triple at 0x[0-9a-f]+> \( 12 \)\n',out)
phi=ex.improve(ex.golden_update,ex.square_close_to_successor)
assert phi==1.6180339887498951 and ex.approx_eq(phi,(1+math.sqrt(5))/2)
assert ex.sqrt(256)==16.0 and ex.square_root_newton(64)==8.0
assert [ex.nth_root_of_a(n,64) for n in [2,3,6]]==[8.0,4.0,2.0]
assert ex.power(3,0)==1 and ex.power(3,4)==81
assert 10-(100-64)/20==8.2
# Bounded stagnation probe; never run the known infinite sqrt10 loop.
x=1
for _ in range(100):x=ex.average(x,10/x)
assert x==3.162277660168379 and ex.average(x,10/x)==x
assert x*x-10==-1.7763568394002505e-15 and not ex.approx_eq(x*x,10)
newton=ex.newton_update(lambda x:x**3-2*x+2,lambda x:3*x*x-2)
assert newton(0)==1 and newton(1)==0
assert output(ex.play_twenty_one,ex.simple_strategy,ex.simple_strategy)==(None,'Player 0 wins the game\n')
assert output(ex.printed(pow),2,8)==(256,'Result: 256\n')
assert output(ex.printed(abs),-10)==(10,'Result: 10\n')
# Original lecture modules, including supplied global f for L3's demo.
lecture_dir=MAT/'sources/cs61a.org/fa26/assets/lec'
lec3=runpy.run_path(str(lecture_dir/'03.py'),init_globals={'f':ex.increment})
out=io.StringIO()
with contextlib.redirect_stdout(out):lec4=runpy.run_path(str(lecture_dir/'04.py'))
assert out.getvalue()==("you're going down!\nthanks for playing with me!\n"*4+'Player 0 wins the game\n')
assert lec4['get_name']('', 'Ousterhout')=='Ousterhout'
assert [lec4['same_length'](a,b) for a,b in [(4,8),(100,657),(4,100),(0,1)]]==[True,True,False,False]
from unittest.mock import patch
with patch('builtins.input',return_value='2'):
    assert output(lec4['interactive_strategy'],10)==(2,'Current score 10 What do you want to play (1-3)?\n')
lecture_runner=doctest.DocTestRunner()
lecture_parser=doctest.DocTestParser()
for namespace,filename in [(lec3,'03.py'),(lec4,'04.py')]:
    for name,obj in namespace.items():
        if callable(obj) and getattr(obj,'__doc__',None) and '>>>' in obj.__doc__:
            lecture_runner.run(lecture_parser.get_doctest(obj.__doc__,namespace,name,filename,0))
assert lecture_runner.summarize().failed==0
ns={};exec("def what_prints():\n print('Hello World!')\n return 'Goodbye.'\n print('What about me?')",ns)
assert output(ns['what_prints'])==('Goodbye.','Hello World!\n')
assert ex.summation(10,ex.identity)==55
# Statement, Boolean, and deliberate-error examples.
assert (0 and 1/0)==0 and (2 or 1/0)==2
assert (2 and 7)==7 and (0 or 7)==7 and (not 0) is True
for op in ['/', '//', '%']:
    try:eval('1'+op+'0')
    except ZeroDivisionError:pass
    else:raise AssertionError('Expected division error')
for a,b,vals in [(1,5,(.2,0,1)),(25,4,(6.25,6,1)),(4,2,(2.0,2,0))]:
    assert (a/b,a//b,a%b)==vals
assert -5//4==-2 and (3579//100)%10==5
# Literal source variants A--F, preserving their defining frames.
base='def make_adder(n):\n{outer}    def adder(k):\n{inner}        return n+k\n{after}    return adder\nadd_three=make_adder(3)\n{global_extra}\nanswer=add_three(4)'
variants=[('    k=5\n','','','',7),('    n=5\n','','','',9),
          ('','        k=5\n','','',8),('','','','add_five=make_adder(5)',7),
          ('','','    n=5\n','',9),('','','','n=5',7)]
for outer,inner,after,global_extra,want in variants:
    ns={};exec(base.format(outer=outer,inner=inner,after=after,global_extra=global_extra),ns)
    assert ns['answer']==want
ns={};exec('def make_adder(n):\n return adder\ndef adder(k):\n return n+k\nadd_three=make_adder(3)',ns)
try:ns['add_three'](4)
except NameError:pass
else:raise AssertionError('Expected missing-global n')
# Actual Lab1 WWPD: prompt displays repr of returned strings, print does not.
assert output(lab.welcome)==('hello','Go\n')
assert output(lambda:print(lab.welcome(),lab.cal()))==(None,'Go\nBears\nhello world\n')
assert output(lab.ab,10,20)==(None,'10\nfoo\n')
assert output(lab.bake,0,5)==(5,'1\n5\n')
assert output(lab.bake,1,'yum')==('yum','yum\n')
assert output(lab.bake,2,3)==(2,'')
assert disc.race(2,3)==15 and disc.race(5,7)==7 and disc.race(2,4)==10
# Race(3,4) first passes at7, then never equals; bounded cycle evidence.
states=[];t=h=0
for minute in range(100):
    t+=3
    if minute%10<5:h+=4
    states.append(t-h)
assert states[6]>0 and all(v!=0 for v in states)
assert states[9]==10 and states[19]==20
assert disc.bottles==disc.remaining==98 and disc.hat(4)==8 and disc.double(4)==12
assert [disc.unique_digits(n) for n in [8675309,13173131,101]]==[7,3,2]
assert disc.has_digit(10,1) and not disc.has_digit(12,7)
assert [disc.repeating(t,6161) for t in range(1,6)]==[False,True,False,True,False]
assert not disc.repeating(2,101) and not disc.repeating(2,10101)
for n in range(1,5001):
    for t in range(1,6):
        text=str(n);want=(len(text)%t==0 and text[:t]*(len(text)//t)==text)
        assert disc.repeating(t,n)==want,(t,n)
for n in range(10000):
    assert lab.double_eights(n)==('88' in str(n))
    assert lab.sum_digits(n)==sum(map(int,str(n)))
# Church numerals: operations must work for arbitrary functions, not just inc.
nums=[hw.zero]
for _ in range(4):nums.append(hw.successor(nums[-1]))
for a,b in itertools.product(range(5),repeat=2):
    assert hw.church_to_int(hw.add_church(nums[a],nums[b]))==a+b
    assert hw.church_to_int(hw.mul_church(nums[a],nums[b]))==a*b
    assert hw.church_to_int(hw.pow_church(nums[a],nums[b]))==a**b
assert hw.two(lambda x:'('+x+')')('z')=='((z))'
# Independent digit-group and adjacent-gap oracles, including zeros inside n.
for n in range(1,2001):
    groups=[]
    for digit in str(n):
        parity=int(digit)%2
        if groups and groups[-1][0]==parity:groups[-1][1]+=1
        else:groups.append([parity,1])
    for k in range(1,6):assert exam.num_long_groups(n,k)==sum(size>=k for _,size in groups)
assert [exam.num_long_groups(15732429999,k) for k in [3,4,5,1]]==[3,2,0,3]
assert [exam.gap(n,f) for n,f in [(5,lambda x:x*x),(6,lambda x:x%4),(4,lambda x:-x)]]==[9,3,1]
assert exam.odd_gap(5,lambda x:x*x)==16 and exam.odd_gap(8,lambda x:x%5)==3
assert [exam.classify(n) for n in [6,24,23]]==['perfect','abundant','deficient']
s='Knock'
assert output(lambda:print(print(print(s,s) or print("Who's There?")),"Who?"))==(None,"Knock Knock\nWho's There?\nNone\nNone Who?\n")
# Hog callback counts, arbitrary-score digits, all state pairs and boundary goals.
die=hog.make_test_dice(4,1,2)
assert [die() for _ in range(5)]==[4,1,2,4,1]
die=hog.make_test_dice(4,1,2,6)
assert hog.roll_dice(3,die)==1 and die()==6
for own,opp,want in [(21,46,9),(45,52,1),(2,5,6),(121,146,9)]:
    assert hog.boar_brawl(own,opp)==want
assert [hog.sus_points(n) for n in [21,64,67]]==[23,64,67]
assert [hog.num_factors(n) for n in [1,2,3,8,9]]==[1,2,2,4,3]
assert hog.sus_update(0,53,60)==67
assert hog.sus_strategy(53,60,14,2)==0 and hog.sus_strategy(53,60,15,2)==2
for value in [1,2,3]:
    assert hog.max_scoring_num_rolls(hog.make_test_dice(value))==(1 if value==1 else 10)
assert hog.max_scoring_num_rolls(hog.make_test_dice(1,2))==1
assert hog.make_averaged(hog.roll_dice,40)(1,hog.make_test_dice(4,2,5,1))==3.0
assert hog.is_always_roll(hog.always_roll(3)) and not hog.is_always_roll(hog.catch_up)
for score,opp in itertools.product(range(100),repeat=2):
    assert 0<=hog.final_strategy(score,opp)<=10
calls=[]
def strategy0(a,b):calls.append(('s0',a,b));return 1
def strategy1(a,b):calls.append(('s1',a,b));return 1
def update(r,a,b,d):calls.append(('u',a,b));return a+2
assert hog.play(strategy0,strategy1,update,goal=3)==(4,2)
assert calls==[('s0',0,0),('u',0,0),('s1',0,2),('u',0,2),('s0',2,2),('u',2,2)]
calls.clear();assert hog.play(strategy0,strategy1,update,score1=3,goal=3)==(0,3) and not calls
# Execute unmodified official tests against filled copies, not original TODOs.
runner=doctest.DocTestRunner(optionflags=doctest.ELLIPSIS)
parser=doctest.DocTestParser()
failures=io.StringIO()
with tempfile.TemporaryDirectory(prefix='cs61a-week2-') as temp:
    temp=Path(temp)
    for assignment,solname in [('lab01','lab_solutions'),('hw02','hw_solutions'),('hog','hog_solutions')]:
        target=temp/assignment
        shutil.copytree(MAT/'starter-code'/assignment,target)
        orig=ast.parse((target/(assignment+'.py')).read_text())
        sol=ast.parse((W/(solname+'.py')).read_text())
        replacements={n.name:n for n in sol.body if isinstance(n,ast.FunctionDef)}
        for node in orig.body:
            if isinstance(node,ast.FunctionDef) and node.name in replacements:
                body=replacements[node.name].body
                if ast.get_docstring(replacements[node.name]):body=body[1:]
                doc=node.body[:1] if ast.get_docstring(node) else []
                node.body=doc+body
        (target/(assignment+'.py')).write_text(ast.unparse(ast.fix_missing_locations(orig))+'\n')
        sys.path.insert(0,str(target))
        for key in list(sys.modules):
            if key=='tests' or key.startswith('tests.'):del sys.modules[key]
        module=load(target/(assignment+'.py'),assignment)
        oldcwd=Path.cwd();os.chdir(target)
        try:
            # All public starter docstrings, retaining inspect-based checks.
            for node in orig.body:
                if isinstance(node,ast.FunctionDef) and node.name in replacements:
                    doc=ast.get_docstring(node)
                    if doc and '>>>' in doc:
                        module=load(target/(assignment+'.py'),assignment)
                        runner.run(parser.get_doctest(doc,module.__dict__,node.name,str(target/(assignment+'.py')),0),out=failures.write)
            # Official test files: locked questions are separate WWPD exercises.
            testdir=target/'tests'
            if testdir.exists():
                for testfile in sorted(testdir.glob('*.py')):
                    tree=ast.parse(testfile.read_text())
                    for node in tree.body:
                        if isinstance(node,ast.FunctionDef):
                            doc=ast.get_docstring(node)
                            if doc and '>>>' in doc and 'LOCKED:' not in doc:
                                load(target/(assignment+'.py'),assignment)  # Isolate official monkeypatch tests.
                                runner.run(parser.get_doctest(doc,{},str(testfile)+':'+node.name,str(testfile),0),out=failures.write)
            if assignment=='hog':
                load(target/'hog.py','hog')
                ui=load(target/'hog_ui.py','week2ui')
                for node in ast.parse((target/'hog_ui.py').read_text()).body:
                    if isinstance(node,ast.FunctionDef):
                        doc=ast.get_docstring(node)
                        if doc and '>>>' in doc:
                            runner.run(parser.get_doctest(doc,ui.__dict__,node.name,str(target/'hog_ui.py'),0),out=failures.write)
        finally:os.chdir(oldcwd);sys.path.pop(0)
res=runner.summarize()
if res.failed:
    print(failures.getvalue()[:5000])
assert res.failed==0,res
print('PASS: all printed executable modules; source numeric/WWPD and error cases;')
print('25,000 repeating cases, 10,000 digit cases, Church grids, exam digit oracle,')
print('Hog callback counts/state boundaries and official tests:',res.attempted,'examples.')
