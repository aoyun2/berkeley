"""Predict the output. Each snippet is run as a FILE (only print displays anything).
Replace each "?" with exactly what is displayed. If the snippet stops with an error,
write the lines displayed before it and then a last line ERROR.
"""

SNIPPETS = {
"p1": '''
print(0 or 7)
print(7 and 0)
print(None or '' or 'x')
print(3 and 4 and 5)
''',
"p2": '''
x = print(1) or print(2)
print(x)
''',
"p3": '''
def f(n):
    if n > 5:
        return 'big'
    if n > 2:
        print('medium')
    return 'small'
print(f(9))
print(f(4))
''',
"p4": '''
i = 0
while i < 6:
    i = i + 2
    print(i)
print('done', i)
''',
"p5": '''
n, total = 4321, 0
while n > 0:
    total = total + n % 10
    n = n // 100
print(total)
''',
"p6": '''
def make(n):
    def f(k):
        return k * n
    return f
double, triple = make(2), make(3)
print(double(triple(5)), make(4)(1))
''',
"p7": '''
def apply(f, x):
    return f(x)
def shout(x):
    print(x, '!')
print(apply(shout, 'hey'))
''',
"p8": '''
def outer(a):
    def inner(b):
        return a - b
    a = a + 10
    return inner
a = 1
g = outer(a)
print(g(a), a)
''',
"p9": '''
def loop(n):
    while n > 0:
        if n % 3 == 0:
            return n
        n = n - 1
print(loop(8), loop(2))
''',
"p10": '''
print(1 / 0 and 1 or 2)
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
"p10": """?""",
}
