"""Timed set: 25 minutes, on paper first. Exam rules: no str, no lists."""


def count_peaks(n):
    """A peak is a digit that is larger than both of its neighbours (so the first
    and last digits are never peaks). Return the number of peaks in positive n.

    >>> count_peaks(13254)      # 3 and 5
    2
    >>> count_peaks(1234)
    0
    >>> count_peaks(121)
    1
    >>> count_peaks(9)
    0
    """
    count = 0
    while n >= 100:
        left, mid, right = n // 100 % 10, n // 10 % 10, n % 10
        if mid > left and mid > right:
            count = count + 1
        n = n // 10
    return count


def twice_if(pred):
    """Return a function that takes a one-argument function f and returns a function
    of x: it returns f(f(x)) if pred(x) is true and f(x) otherwise.

    >>> inc = lambda x: x + 1
    >>> g = twice_if(lambda x: x % 2 == 0)(inc)
    >>> g(4), g(5)
    (6, 6)
    """
    def take(f):
        return lambda x: f(f(x)) if pred(x) else f(x)
    return take


def first_agree(f, g):
    """Return the smallest positive integer k with f(k) == g(k). Assume one exists.

    >>> first_agree(lambda k: k * k, lambda k: 3 * k + 4)
    4
    >>> first_agree(lambda k: k % 5, lambda k: 0)
    5
    """
    k = 1
    while f(k) != g(k):
        k = k + 1
    return k
