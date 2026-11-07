"""Authentic exam inputs and constrained completed functions."""

# BEGIN new_print
def new_print(print):
    def f(x):
        value = print(x)
        if value != None:
            return print('What?')
        return x
    return f
# END new_print

# BEGIN gap_tool
def gap(n, term):
    k, largest = 1, 0
    while k < n:
        largest = max(largest, abs(term(k + 1) - term(k)))
        k = k + 1
    return largest
# END gap_tool

# BEGIN make_gap
def f(use, go, then):
    y, i = 0, 0
    while go(y, i):
        i += 1
        if use(i):
            y += 1
    return then(y, i)

def make_gap(use):
    return lambda n, term: gap(
        f(use, lambda y, i: i < n, lambda y, i: y),
        lambda j: term(f(use, lambda y, i: y < j,
                         lambda y, i: i)))
# END make_gap

# BEGIN funsquare
def funsquare_A(f):
    return f(f)

def funsquare_B(f):
    return lambda: f(f)

def funsquare_C(f, x):
    def g(x):
        return f(f(x))
    return g

def funsquare_D(f):
    return lambda x: f(f(x))

def funsquare_E(f, x):
    return f(f(x))

def funsquare_F(f):
    def g(x):
        return f(f(x))
    return g
# END funsquare
