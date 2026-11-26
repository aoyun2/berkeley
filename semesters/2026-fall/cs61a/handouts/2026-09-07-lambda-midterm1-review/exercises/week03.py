"""CS 61A Week 3 timed practice: lambda, currying, and closures."""


def curry_binary(f):
    """Return the curried version of binary function f: curry_binary(f)(x)(y) == f(x, y)."""
    raise NotImplementedError("TODO: implement curry_binary")


def repeat_until(f, stop):
    """Return a one-argument function h such that h(x) is the first value v in the
    sequence x, f(x), f(f(x)), ... for which stop(v) is true. If stop(x) is already
    true, h(x) is x itself (f is applied zero times). Assume some value satisfies stop."""
    raise NotImplementedError("TODO: implement repeat_until")


def make_alternator(f, g):
    """Return h(n) equal to f(n) when n is even and g(n) when n is odd."""
    raise NotImplementedError("TODO: implement make_alternator")


def max_over_range(fn, lo, hi):
    """Independent transfer: return the maximum of fn(k) for integers k in [lo, hi] (lo <= hi)."""
    raise NotImplementedError("TODO: implement max_over_range")
