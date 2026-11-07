"""HW2 required and just-for-fun solutions, with inspectable source."""
# BEGIN hw_helpers
from operator import add, mul

def square(x):
    return x * x

def identity(x):
    return x

def triple(x):
    return 3 * x

def increment(x):
    return x + 1
# END hw_helpers

# BEGIN product
def product(n, term):
    """Return the product of term(1) through term(n)."""
    result, k = 1, 1
    while k <= n:
        result, k = result * term(k), k + 1
    return result
# END product

# BEGIN accumulate
def accumulate(fuse, start, n, term):
    """Combine start with the first n terms using fuse."""
    result, k = start, 1
    while k <= n:
        result, k = fuse(result, term(k)), k + 1
    return result


def summation_using_accumulate(n, term):
    """Sum the first n terms using accumulate."""
    return accumulate(add, 0, n, term)


def product_using_accumulate(n, term):
    """Multiply the first n terms using accumulate."""
    return accumulate(mul, 1, n, term)
# END accumulate

# BEGIN repeater
def make_repeater(f, n):
    def repeated(x):
        count = 0
        while count < n:
            x, count = f(x), count + 1
        return x
    return repeated
# END repeater

# BEGIN composite
def composite_identity(f, g):
    def equal_at(x):
        return f(g(x)) == g(f(x))
    return equal_at
# END composite

# BEGIN church_basic
def zero(f):
    return lambda x: x


def successor(n):
    return lambda f: lambda x: f(n(f)(x))


def one(f):
    return lambda x: f(x)


def two(f):
    return lambda x: f(f(x))


three = successor(two)


def church_to_int(n):
    return n(lambda x: x + 1)(0)
# END church_basic

# BEGIN church_arithmetic
def add_church(m, n):
    return lambda f: lambda x: m(f)(n(f)(x))


def mul_church(m, n):
    return lambda f: m(n(f))


def pow_church(m, n):
    return n(m)
# END church_arithmetic
