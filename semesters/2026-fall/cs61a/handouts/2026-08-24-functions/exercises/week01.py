"""CS 61A Week 1 exercises: expressions, names, def, return, print.

Rules: no if, while, for, and, or. Use only arithmetic, calls, def, return, print.
"""
from math import sqrt


def seconds_in(days, hours, minutes):
    """Return the number of seconds in the given days, hours and minutes.

    >>> seconds_in(0, 0, 1)
    60
    >>> seconds_in(1, 1, 1)
    90060
    """
    "*** YOUR CODE HERE ***"


def last_two_sum(n):
    """Return the sum of the last two digits of the positive integer n (n >= 10).

    >>> last_two_sum(2026)
    8
    >>> last_two_sum(90)
    9
    """
    "*** YOUR CODE HERE ***"


def swap_digits(n):
    """Return the two-digit number n (10 <= n <= 99) with its digits exchanged.

    >>> swap_digits(27)
    72
    >>> swap_digits(40)
    4
    """
    "*** YOUR CODE HERE ***"


def spread(a, b, c):
    """Return the difference between the largest and the smallest of a, b, c.
    Use a single return statement.

    >>> spread(3, 10, 5)
    7
    >>> spread(4, 4, 4)
    0
    """
    "*** YOUR CODE HERE ***"


def clamp(x, low, high):
    """Return x if low <= x <= high, low if x is below low, and high if x is above high.
    Assume low <= high. Use a single return statement.

    >>> clamp(5, 0, 10)
    5
    >>> clamp(-3, 0, 10)
    0
    >>> clamp(42, 0, 10)
    10
    """
    "*** YOUR CODE HERE ***"


def distance(x1, y1, x2, y2):
    """Return the distance between the points (x1, y1) and (x2, y2).

    >>> distance(0, 0, 3, 4)
    5.0
    >>> distance(1, 1, 1, 1)
    0.0
    """
    "*** YOUR CODE HERE ***"


def is_multiple(n, d):
    """Return True if d divides n evenly and False otherwise. No if statement:
    a comparison is already an expression with a True/False value.

    >>> is_multiple(12, 4)
    True
    >>> is_multiple(12, 5)
    False
    """
    "*** YOUR CODE HERE ***"


def report(celsius):
    """Print one line 'C = <celsius> F = <fahrenheit>' and return the Fahrenheit
    value, where fahrenheit = celsius * 9 / 5 + 32.

    >>> f = report(100)
    C = 100 F = 212.0
    >>> f
    212.0
    >>> report(report(-40))
    C = -40 F = -40.0
    C = -40.0 F = -40.0
    -40.0
    """
    "*** YOUR CODE HERE ***"


def trace_add(a, b):
    """Print 'adding a b' (with the values) and return a + b.

    >>> trace_add(trace_add(1, 2), trace_add(3, 4))
    adding 1 2
    adding 3 4
    adding 3 7
    10
    """
    "*** YOUR CODE HERE ***"
