"""Predict the output. Each snippet is run as a FILE (only print displays anything).
Replace each "?" with exactly what is displayed (ERROR as a last line if it errors).
"""

SNIPPETS = {
"p1": '''
def f(n):
    if n < 10:
        return n
    return f(n // 10) * 10
print(f(4567))
''',
"p2": '''
def g(n):
    print(n)
    if n > 1:
        g(n - 2)
    print(n)
g(5)
''',
"p3": '''
def h(n):
    if n == 0:
        return 0
    h(n - 1) + 1
print(h(3))
''',
"p4": '''
def t(n):
    if n <= 1:
        return 1
    return t(n - 1) + t(n - 2)
print(t(5))
''',
"p5": '''
def calls(n):
    print('call', n)
    if n <= 1:
        return n
    return calls(n - 1) + calls(n - 2)
print(calls(3))
''',
"p6": '''
def outer(n):
    def inner(k):
        if k == n:
            return k
        return inner(k + 1)
    return inner(0)
print(outer(4))
''',
"p7": '''
def even(n):
    return n == 0 or odd(n - 1)
def odd(n):
    return n != 0 and even(n - 1)
print(even(3), odd(3))
''',
"p8": '''
def bad(n):
    return bad(n - 1) if n > 0 else bad(n + 1)
print('start')
print(bad(2))
''',
}

PREDICTIONS = {
"p1": """4000""",
"p2": """5
3
1
1
3
5""",
"p3": """ERROR""",
"p4": """8""",
"p5": """call 3
call 2
call 1
call 0
call 1
2""",
"p6": """4""",
"p7": """False True""",
"p8": """start
ERROR""",
}
