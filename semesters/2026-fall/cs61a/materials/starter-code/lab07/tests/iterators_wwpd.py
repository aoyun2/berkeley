from pytest_grader import points


@points(0)
def iterators_wwpd():
    """What Would Python Display?

    >>> s = [1, 2, 3, 4]
    >>> t = iter(s)
    >>> next(s)
    LOCKED: 6ae2f2793ea71f56
    >>> next(t)
    LOCKED: d2ab7f9baff9b024
    >>> next(t)
    LOCKED: 5a3e8fcaec83c79a
    >>> next(iter(s))
    LOCKED: 950a795edaf6a320
    >>> next(iter(s))
    LOCKED: 95fc2b8f105e64d2
    >>> u = t
    >>> next(u)
    LOCKED: abfbe2a161514bf9
    >>> next(t)
    LOCKED: 55f75a1d2245add9

    >>> r = range(6)
    >>> r_iter = iter(r)
    >>> next(r_iter)
    LOCKED: f65a5887b441999d
    >>> [x + 1 for x in r]
    LOCKED: 094586fd8969275b
    >>> [x + 1 for x in r_iter]
    LOCKED: 129b32ce81354e72
    >>> next(r_iter)
    LOCKED: f999692e74bdb41d

    >>> map_iter = map(lambda x : x + 10, range(5))
    >>> next(map_iter)
    LOCKED: 80993a515f9d3385
    >>> next(map_iter)
    LOCKED: 89de5dfb30072fd4
    >>> list(map_iter)
    LOCKED: b85aa0680428fdba
    >>> for e in filter(lambda x : x % 4 == 0, range(1000, 1008)):
    ...     print(e)
    LOCKED: e39e9db6b648f709
    LOCKED: 18efd2a1085ce906
    >>> [x + y for x, y in zip([1, 2, 3], [4, 5, 6])]
    LOCKED: a2e298eef8f79f5e
    """
