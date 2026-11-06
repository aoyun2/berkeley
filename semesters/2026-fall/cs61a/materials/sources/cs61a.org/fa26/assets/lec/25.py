from link import *

def squares(n) -> LinkedList[int]:
    """A linked list of n positive perfect squares.

    >>> print(squares(10))
    (1 4 9 16 25 36 49 64 81 100)
    """
    def f(i):
        if i > n:
            return ()
        else:
            return Link(i*i, f(i+1))
    return f(1)

def low_squares(n) -> LinkedList[int]:
    """A linked list of n positive perfect squares with ones digits below 5.

    >>> print(low_squares(10))
    (1 4 25 64 81 100 121 144 225 324)
    """
    def f(i, k):
        if k == n:
            return ()
        elif i * i % 10 <= 5:
            return Link(i*i, f(i+1, k+1))
        else:
            return f(i+1, k)
    return f(1, 0)
           
def slice_link(s: LinkedList, i, j) -> LinkedList:
    """Return a linked list containing elements from i:j.

    >>> evens = Link(4, Link(2, Link(6)))
    >>> print(slice_link(evens, 1, 100))
    (2 6)
    >>> print(slice_link(evens, 1, 2))
    (2)
    >>> print(slice_link(evens, 0, 2))
    (4 2)
    >>> slice_link(evens, 1, 1)
    ()
    """
    assert i >= 0 and j >= 0
    if j == 0 or s == ():
        return ()
    elif i == 0:
        return Link(s.first, slice_link(s.rest, 0, j-1))
    else:
        return slice_link(s.rest, i-1 , j-1)

