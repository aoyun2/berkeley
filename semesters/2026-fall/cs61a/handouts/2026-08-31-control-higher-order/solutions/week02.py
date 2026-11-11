"""CS 61A Week 2 exercises: if, and/or, while, higher-order functions."""


def grade(score):
    """Return 'A' for 90 and above, 'B' for 80-89, 'C' for 70-79 and 'F' below 70.

    >>> grade(95)
    'A'
    >>> grade(80)
    'B'
    >>> grade(79)
    'C'
    >>> grade(12)
    'F'
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'F'


def count_digit(n, d):
    """Return how many times the digit d appears in the positive integer n.

    >>> count_digit(2026, 2)
    2
    >>> count_digit(2026, 7)
    0
    >>> count_digit(5, 5)
    1
    """
    count = 0
    while n > 0:
        if n % 10 == d:
            count = count + 1
        n = n // 10
    return count


def reverse_number(n):
    """Return the positive integer n with its digits in reverse order.

    >>> reverse_number(2026)
    6202
    >>> reverse_number(7)
    7
    >>> reverse_number(120)
    21
    """
    result = 0
    while n > 0:
        result = result * 10 + n % 10
        n = n // 10
    return result


def largest_digit(n):
    """Return the largest digit of the positive integer n. Do not use if.

    >>> largest_digit(2026)
    6
    >>> largest_digit(909)
    9
    """
    largest = 0
    while n > 0:
        largest = max(largest, n % 10)
        n = n // 10
    return largest


def gcd(a, b):
    """Return the greatest common divisor of positive integers a and b, using
    the fact that gcd(a, b) == gcd(b, a % b) and gcd(a, 0) == a.

    >>> gcd(12, 18)
    6
    >>> gcd(17, 5)
    1
    >>> gcd(100, 10)
    10
    """
    while b > 0:
        a, b = b, a % b
    return a


def first_power_above(base, limit):
    """Return the smallest non-negative integer k with base ** k > limit (base > 1).

    >>> first_power_above(2, 1000)
    10
    >>> first_power_above(10, 5)
    1
    >>> first_power_above(3, 0)
    0
    """
    k, power = 0, 1
    while power <= limit:
        k, power = k + 1, power * base
    return k


def is_increasing(n):
    """Return True if the digits of n strictly increase from left to right.

    >>> is_increasing(1359)
    True
    >>> is_increasing(1339)
    False
    >>> is_increasing(8)
    True
    >>> is_increasing(91)
    False
    """
    while n >= 10:
        if n // 10 % 10 >= n % 10:
            return False
        n = n // 10
    return True


def sum_where(n, term, keep):
    """Return the sum of term(k) over those k in 1..n for which keep(k) is a true value.

    >>> def square(k): return k * k
    >>> def odd(k): return k % 2 == 1
    >>> sum_where(5, square, odd)     # 1 + 9 + 25
    35
    >>> def always(k): return True
    >>> sum_where(4, square, always)
    30
    """
    total, k = 0, 1
    while k <= n:
        if keep(k):
            total = total + term(k)
        k = k + 1
    return total


def nth_where(n, keep):
    """Return the n-th positive integer k (n >= 1) for which keep(k) is a true value.

    >>> def odd(k): return k % 2 == 1
    >>> nth_where(4, odd)
    7
    >>> def big(k): return k > 100
    >>> nth_where(1, big)
    101
    """
    k, found = 0, 0
    while found < n:
        k = k + 1
        if keep(k):
            found = found + 1
    return k


def make_between(low, high):
    """Return a one-argument function that returns True exactly when its argument x
    satisfies low <= x <= high.

    >>> teen = make_between(13, 19)
    >>> teen(13), teen(16), teen(20)
    (True, True, False)
    >>> make_between(0, 0)(0)
    True
    """
    def between(x):
        return low <= x and x <= high
    return between


def compose3(f, g, h):
    """Return the function that maps x to f(g(h(x))).

    >>> def inc(x): return x + 1
    >>> def double(x): return 2 * x
    >>> compose3(inc, double, inc)(5)      # inc(double(inc(5)))
    13
    """
    def composed(x):
        return f(g(h(x)))
    return composed


def make_logged(f, label):
    """Return a function that behaves like the one-argument function f, but each
    time it is called it first prints label and its argument. f must be called
    exactly once per call.

    >>> def double(x): return 2 * x
    >>> d = make_logged(double, 'double')
    >>> d(d(3))
    double 3
    double 6
    12
    """
    def logged(x):
        print(label, x)
        return f(x)
    return logged


def either(f, g):
    """Return a function of x that returns f(x) if that is a true value and
    otherwise returns g(x). g must not be called when f(x) is a true value.
    The body of the inner function is one return statement with no if.

    >>> def half(x): return x // 2
    >>> def loud(x):
    ...     print('called loud')
    ...     return -x
    >>> e = either(half, loud)
    >>> e(10)
    5
    >>> e(1)
    called loud
    -1
    """
    def choose(x):
        return f(x) or g(x)
    return choose
