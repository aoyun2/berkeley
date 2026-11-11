"""Predict the output. Each snippet is run as a FILE (so only print displays anything).
Replace each "?" with exactly what is displayed, one output line per line of your string.
If the snippet stops with an error, write the lines displayed before it, then a last line ERROR.
"""

SNIPPETS = {
"p1": '''
x = 4
y = x * 2
x = y - x
print(x, y)
''',
"p2": '''
def f(x):
    x = x + 1
    return x * 2
x = 5
y = f(x)
print(x, y)
''',
"p3": '''
print(print(1), print(2, 3))
''',
"p4": '''
def shout(s):
    print(s, s)
a = shout('hi')
print(a)
''',
"p5": '''
from operator import add, mul
print(add(mul(2, 3), mul(add(1, 1), 5)))
''',
"p6": '''
def g(a, b):
    b = a
    a = b + 1
    return a + b
a = 1
b = 10
print(g(b, a), a, b)
''',
"p7": '''
def inc(n):
    print('inc', n)
    return n + 1
print(inc(inc(1)) + inc(10))
''',
"p8": '''
big = max
max = min
print(max(2, 9), big(2, 9))
print(7 // 2, 7 % 2, 7 / 2, 2 ** 3)
''',
"p9": '''
def k(n):
    print(n)
print(k(1) + 1)
''',
}

PREDICTIONS = {
"p1": """?""",
"p2": """?""",
"p3": """?""",
"p4": """?""",
"p5": """?""",
"p6": """?""",
"p7": """?""",
"p8": """?""",
"p9": """?""",
}
