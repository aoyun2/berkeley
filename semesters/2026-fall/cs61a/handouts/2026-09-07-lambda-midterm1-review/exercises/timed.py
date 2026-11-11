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
    "*** YOUR CODE HERE ***"


def twice_if(pred):
    """Return a function that takes a one-argument function f and returns a function
    of x: it returns f(f(x)) if pred(x) is true and f(x) otherwise.

    >>> inc = lambda x: x + 1
    >>> g = twice_if(lambda x: x % 2 == 0)(inc)
    >>> g(4), g(5)
    (6, 6)
    """
    "*** YOUR CODE HERE ***"


def first_agree(f, g):
    """Return the smallest positive integer k with f(k) == g(k). Assume one exists.

    >>> first_agree(lambda k: k * k, lambda k: 3 * k + 4)
    4
    >>> first_agree(lambda k: k % 5, lambda k: 0)
    5
    """
    "*** YOUR CODE HERE ***"
