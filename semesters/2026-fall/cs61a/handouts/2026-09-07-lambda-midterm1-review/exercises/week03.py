"""CS 61A Week 3 exercises: lambda, currying, zero-argument functions, iteration."""


def make_between(low, high):
    """Return a function of x that is True exactly when low <= x <= high.
    The body is one lambda expression.

    >>> teen = make_between(13, 19)
    >>> teen(13), teen(20)
    (True, False)
    """
    "*** YOUR CODE HERE ***"


def uncurry(g):
    """g is a curried two-argument function: g(x)(y). Return the ordinary
    two-argument function f with f(x, y) == g(x)(y). One lambda expression.

    >>> curried_pow = lambda x: lambda y: pow(x, y)
    >>> uncurry(curried_pow)(2, 5)
    32
    """
    "*** YOUR CODE HERE ***"


def flip_curried(g):
    """g is curried: g(x)(y). Return the curried function h with h(y)(x) == g(x)(y).
    One lambda expression.

    >>> minus = lambda x: lambda y: x - y
    >>> flip_curried(minus)(1)(10)
    9
    """
    "*** YOUR CODE HERE ***"


def repeat_until(f, done):
    """Return a function of x that applies f to x again and again until done(result)
    is a true value, and returns that result. If done(x) is already true, x is returned.

    >>> halve_to_odd = repeat_until(lambda x: x // 2, lambda x: x % 2 == 1)
    >>> halve_to_odd(40)
    5
    >>> halve_to_odd(7)
    7
    """
    "*** YOUR CODE HERE ***"


def lazy_or(first, second):
    """first and second are ZERO-argument functions. Return first() if it is a true
    value; otherwise return second(). second must not be called if first() is true.
    One return statement, no if.

    >>> def loud():
    ...     print('second was called')
    ...     return 7
    >>> lazy_or(lambda: 3, loud)
    3
    >>> lazy_or(lambda: 0, loud)
    second was called
    7
    """
    "*** YOUR CODE HERE ***"


def cycle(a, b, c):
    """PROVIDED, do not change: return a zero-argument function that returns
    a, b, c, a, b, c, ... on successive calls.

    >>> d = cycle(1, 2, 3)
    >>> d(), d(), d(), d()
    (1, 2, 3, 1)
    """
    state = [0]
    def next_value():
        state[0] += 1
        return (a, b, c)[(state[0] - 1) % 3]
    return next_value


def calls_until_repeat(source):
    """source is a zero-argument function. Call it until it returns the same value
    twice in a row; return the total number of calls made.

    >>> calls_until_repeat(cycle(4, 4, 9))      # 4, 4
    2
    >>> calls_until_repeat(cycle(1, 2, 2))      # 1, 2, 2
    3
    >>> calls_until_repeat(cycle(5, 6, 5))      # 5, 6, 5, 5
    4
    """
    "*** YOUR CODE HERE ***"


def digit_filter(n, keep):
    """Return the number formed by the digits d of positive n for which keep(d) is
    true, in their original order. Return 0 if no digit is kept.

    >>> digit_filter(123456, lambda d: d % 2 == 0)
    246
    >>> digit_filter(9081, lambda d: d > 5)
    98
    >>> digit_filter(111, lambda d: d > 5)
    0
    """
    "*** YOUR CODE HERE ***"


def longest_run(n):
    """Return the length of the longest run of equal consecutive digits in positive n.
    Do not write if.

    >>> longest_run(1223334)
    3
    >>> longest_run(5)
    1
    >>> longest_run(7755777)
    3
    """
    "*** YOUR CODE HERE ***"


def argmax(n, f):
    """Return the k in 1..n for which f(k) is largest (the smallest such k on ties).

    >>> argmax(10, lambda k: -(k - 4) * (k - 4))
    4
    >>> argmax(5, lambda k: k % 3)
    2
    """
    "*** YOUR CODE HERE ***"
