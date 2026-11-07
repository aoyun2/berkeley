"""Executable examples printed in the Week 3 handout."""

# BEGIN summation
def summation(n, term):
    common_ratio = 1/4
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total
# END summation

# BEGIN twice
def twice(f):
    def g(x):
        return f(f(x))
    return g

def square(y):
    return y * y
# END twice

# BEGIN retained
common_ratio = 1/2

def get_term(common_ratio):
    def term(k):
        return pow(common_ratio, k)
    return term

common_ratio = 1/3
term = get_term(common_ratio)
common_ratio = 1/5
# END retained

# BEGIN curry
def curry(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g
# END curry


def is_prime(n):
    if n < 2:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

# BEGIN nearest
def nearest_prime(n):
    k = 0
    while True:
        if is_prime(n + k):
            return n + k
        if k > 0:
            k = -k
        else:
            k = -k + 1
# END nearest
