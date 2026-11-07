"""Completed Lab2 code; original tests are retained by the verifier."""

# BEGIN piecewise
def piecewise(f, g, b):
    def h(x):
        return f(x) if x < b else g(x)
    return h
# END piecewise

# BEGIN count_cond
def count_cond(condition):
    def count(n):
        total, i = 0, 1
        while i <= n:
            if condition(n, i):
                total += 1
            i += 1
        return total
    return count
# END count_cond

# BEGIN cycle
def cycle(f1, f2, f3):
    def g(n):
        def h(x):
            i = 0
            while i < n:
                if i % 3 == 0:
                    x = f1(x)
                elif i % 3 == 1:
                    x = f2(x)
                else:
                    x = f3(x)
                i += 1
            return x
        return h
    return g
# END cycle

# BEGIN lab_diagram
n = 7

def f(x):
    n = 8
    return x + 1

def g(x):
    n = 9
    def h():
        return x + 1
    return h

def f(f, x):
    return f(x + n)

f = f(g, n)
g = (lambda y: y())(f)
# END lab_diagram
