"""Executable Week2 lecture/reading examples; adapted names are stated in text."""

# BEGIN print_once
def increment(x):
    return x + 1


def print_once(x, f):
    y = f(x)
    print(y)
    return y
# END print_once

# BEGIN basic_reading
def percent_difference(x, y):
    difference = abs(x - y)
    return 100 * difference / x


def absolute_value(x):
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x
# END basic_reading

# BEGIN fib
def fib(n):
    """Return Fibonacci number n, for n >= 1."""
    pred, curr = 0, 1
    k = 1
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr
# END fib

# BEGIN prime_factors
def smallest_factor(n):
    k = 2
    while n % k != 0:
        k = k + 1
    return k


def prime_factors(n):
    while n > 1:
        k = smallest_factor(n)
        print(k)
        n = n // k
# END prime_factors

# BEGIN pressure
def pressure(v, t, n=6.022e23):
    """Return ideal-gas pressure in pascals; v in m^3, t in K."""
    k = 1.38e-23  # Boltzmann's constant
    return n * k * t / v
# END pressure

# BEGIN sums
def square(x):
    return x * x


def cube(x):
    return x * x * x


def identity(x):
    return x


def pi_term(k):
    return 8 / ((4*k - 3) * (4*k - 1))


def summation(n, term):
    """Sum term(1) through term(n)."""
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total
# END sums

# BEGIN apply_twice
def apply_twice(f, x):
    return f(f(x))
# END apply_twice

# BEGIN adder
def make_adder(n):
    def adder(k):
        return k + n
    return adder


three_more_than = make_adder(3)
result = three_more_than(4)
# END adder

# BEGIN compose
def compose1(f, g):
    def h(x):
        return f(g(x))
    return h
# END compose

# BEGIN lambda
square_lambda = lambda x: x * x
compose_lambda = lambda f, g: lambda x: f(g(x))
# END lambda

# BEGIN curry
def curried_pow(x):
    def h(y):
        return pow(x, y)
    return h


def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g


def uncurry2(g):
    def f(x, y):
        return g(x)(y)
    return f


def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start = start + 1
# END curry

# BEGIN trace
def trace(fn):
    def wrapped(x):
        print('-> ', fn, '(', x, ')')
        return fn(x)
    return wrapped


@trace
def triple(x):
    return 3 * x
# END trace

# BEGIN improve
def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance


def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess


def golden_update(guess):
    return 1 / guess + 1


def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)
# END improve

# BEGIN sqrt
def average(x, y):
    return (x + y) / 2


def sqrt(a):
    def sqrt_update(x):
        return average(x, a / x)
    def sqrt_close(x):
        return approx_eq(x * x, a)
    return improve(sqrt_update, sqrt_close)
# END sqrt

# BEGIN newton
def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)
    return update


def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)
# END newton

# BEGIN roots
def square_root_newton(a):
    def f(x):
        return x * x - a
    def df(x):
        return 2 * x
    return find_zero(f, df)


def power(x, n):
    product, k = 1, 0
    while k < n:
        product, k = product * x, k + 1
    return product


def nth_root_of_a(n, a):
    def f(x):
        return power(x, n) - a
    def df(x):
        return n * power(x, n - 1)
    return find_zero(f, df)
# END roots

# BEGIN twenty_one
def simple_strategy(score):
    if score < 15:
        return 3
    return 2


def make_heckling_strategy(strategy, heckle):
    def heckling_strategy(s):
        print(heckle)
        return strategy(s)
    return heckling_strategy


def play_twenty_one(strategy0, strategy1):
    current_score, current_player = 0, 0
    while current_score < 21:
        if current_player == 0:
            current_score += strategy0(current_score)
        else:
            current_score += strategy1(current_score)
        current_player = 1 - current_player
    print('Player', current_player, 'wins the game')
# END twenty_one

# BEGIN printed
def printed(f):
    def print_and_return(*args):
        result = f(*args)
        print('Result:', result)
        return result
    return print_and_return
# END printed
