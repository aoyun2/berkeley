def get_n(t, n):
    """ Return a list of the next n iterms from iterator t.
    
    >>> t = iter(range(1000000000))
    >>> get_n(t, 10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    return [next(t) for _ in range(n)]

def yield_ints(start):
    """ Yield all integers, expanding from start.
    
    >>> t = yield_ints(100)
    >>> [next(t), next(t), next(t), next(t), next(t)]
    [100, 101, 99, 102, 98]
    """
    yield start
    offset = 1
    while True:
        yield start + offset
        yield start - offset
        offset += 1

def cycle(s):
    """Iterate over the elements of s repeatedly.

    >>> t = cycle([3, 4, 5])
    >>> [next(t) for _ in range(10)]
    [3, 4, 5, 3, 4, 5, 3, 4, 5, 3]
    """
    while True:
        for x in s:
            yield x

def print_cycle(n, s):
    """ Prints the first n items of the k-cycle sequence that
    repeats the items of s, where k = len(s), but only the items
    at odd indices (1, 3, 5, ...).
    
    >>> pi = [3, 1, -4, -1, 5]
    >>> print_cycle(7, pi)  # 3 [1] -4 [-1] 5 [3] 1
    1
    -1
    3
    >>> print_cycle(1, pi)  # 3
    >>> print_cycle(5, [5, 7])  # 5 [7] 5 [7] 5
    7
    7
    """
    t = cycle(s)
    for i in range(n):
        x = next(t)
        if i % 2 == 1:
            print(x)

def park(n):
    """Return the ways to park cars and motorcycles in n adjacent spots.

    >>> list(park(1))
    ['%', '.']
    >>> list(park(2))
    ['%%', '%.', '.%', '..', '<>']
    >>> list(park(3))
    ['%%%', '%%.', '%.%', '%..', '%<>', '.%%', '.%.', '..%', '...', '.<>', '<>%', '<>.']
    >>> len(list(park(4)))
    29
    """
    if n == 0:
        yield ''
    elif n > 0:
        for s in park(n - 1):
            yield '%' + s
            yield '.' + s
        for s in park(n - 2):
            yield '<>' + s
        #return (['%'  + s for s in park(n-1)] +
        #        ['.'  + s for s in park(n-1)] +
        #        ['<>' + s for s in park(n-2)])

def check_sequence(check):
    """
    >>> t = check_sequence(lambda x, y: y > x)
    >>> [next(t) for i in range(4)]
    [1, 2, 4, 5]
    """
    previous = 1
    while(True):
        if (previous % 3 != 0):
            yield(previous)
        i = 1
        while not check(previous, i):
            i += 1
        previous = i

def print_check_sequence(check, n):
    """Implement print_check_sequence, which takes a two-argument function check and a
    positive integer n, and prints the first n terms of the check sequence that are not
    multiples of 3, one per line

    >>> print_check_sequence(lambda x, y: y > x, 4)  # [1] [2] 3 [4] [5]
    1
    2
    4
    5
    >>> print_check_sequence(lambda x, y: y > 2 * x, 3)  # [1] 3 [7] 15 [31]
    1
    7
    31
    >>> print_check_sequence(lambda x, y: (y == x - 2 or y > x + 10), 4)  # [1] 12 [10] [8] 6 [4]
    1
    10
    8
    4
    """
    t = check_sequence(check)
    for _ in range(n):
        print(next(t))