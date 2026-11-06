class CallCounter:
    def __init__(self):
        self.n = 0

    def count(self, f):
        def counted(n):
            self.n += 1
            return f(n)
        return counted
    
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

from link import *
from timeit import timeit

def partition(n, m) -> list[LinkedList[int]]:
    """Partitions of n using parts up to size m."""
    if n == 0:
        return [()]  # partition 0 with an empty linked list
    elif n < 0 or m == 0:
        return []    # no way to partition these
    with_m = [Link(m, s) for s in partition(n-m, m)]
    without = partition(n, m-1)
    return with_m + without

def print_partitions(k):
    """Print partitions of k.

    >>> print_partitions(6)
    (6)
    (5 1)
    (4 2)
    (4 1 1)
    (3 3)
    (3 2 1)
    (3 1 1 1)
    (2 2 2)
    (2 2 1 1)
    (2 1 1 1 1)
    (1 1 1 1 1 1)
    """
    for s in partition(k, k):
        print(s)

def powers(b):
    """Yield the powers of b."""
    n = 0
    while True:
        yield pow(b, n)
        n += 1

def prefix(t, n):
    """Yield the first n items of an infinite iterator t.

    >>> list(prefix(powers(2), 10))
    [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    """
    while n > 0:
        yield next(t)
        n -= 1

from operator import add

def map_pairs(f, t):
    """Yield the result of calling f on each pair of consecutive items in t.

    >>> list(map_pairs(add, iter([3, 4, 5, 6, 7])))
    [7, 9, 11, 13]
    >>> list(prefix(map_pairs(lambda x, y: (x, y), powers(2)), 5))
    [(1, 2), (2, 4), (4, 8), (8, 16), (16, 32)]
    """
    previous = next(t)
    for x in t:
        yield f(previous, x)
        previous = x

def link_gen(s: LinkedList):
    """Yield the items in a linked list.

    >>> nums = Link(3, Link(5, Link(7)))
    >>> sum(link_gen(nums))
    15
    """
    while isinstance(s, Link):
        yield s.first
        s = s.rest

from tree import *

def labels(t: Tree):
    """Yield the labels of a tree.

    >>> list(labels(Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5)])))
    [1, 2, 3, 4, 5]
    """
    yield t.label
    for b in t.branches:
        yield from labels(b)
