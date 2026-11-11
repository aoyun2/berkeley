"""Predict the output. Each snippet is run as a FILE (only print displays anything).
Replace each "?" with exactly what is displayed (ERROR as a last line if it errors).
"""

SNIPPETS = {
"p1": '''
f = lambda x: lambda y: x * y
print(f(3)(4), f(2)(f(1)(5)))
''',
"p2": '''
a = 2
g = lambda x: x + a
a = 10
print(g(1))
''',
"p3": '''
h = lambda: print('hi')
x = h
y = h()
print(x == h, y)
''',
"p4": '''
def make(n):
    return lambda: n + 1
n = 7
m = make(1)
print(m(), make(n)())
''',
"p5": '''
print((lambda a, b: a if a > b else b)(3, 8))
print(bool(' '), bool(''), bool(0.0), bool(-1))
''',
"p6": '''
max = lambda a, b: a + b
print(max(2, 3))
print(max(1, 2, 3))
''',
"p7": '''
curry = lambda f: lambda x: lambda y: f(x, y)
p = curry(pow)
print(p(2)(3), p(3)(2))
''',
"p8": '''
def apply_twice(f, x):
    return f(f(x))
print(apply_twice(lambda s: s + '!', 'go'))
print(apply_twice(lambda t: print(t), 'once'))
''',
}

PREDICTIONS = {
"p1": """12 10""",
"p2": """11""",
"p3": """hi
True None""",
"p4": """2 8""",
"p5": """8
True False False True""",
"p6": """5
ERROR""",
"p7": """8 9""",
"p8": """go!!
once
None
None""",
}
