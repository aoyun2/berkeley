"""CS 61A Week 3 timed practice: lambda, currying, and closures."""


def curry_binary(f):
    """Return the curried version of binary function f: curry_binary(f)(x)(y) == f(x, y)."""
    raise NotImplementedError("TODO: implement curry_binary")


def compose_n(f, n):
    """Return f applied n times for integer n >= 0 (n=0 is the identity function)."""
    raise NotImplementedError("TODO: implement compose_n")


def make_alternator(f, g):
    """Return h(n) equal to f(n) when n is even and g(n) when n is odd."""
    raise NotImplementedError("TODO: implement make_alternator")


def max_over_range(fn, lo, hi):
    """Independent transfer: return the maximum of fn(k) for integers k in [lo, hi] (lo <= hi)."""
    raise NotImplementedError("TODO: implement max_over_range")
