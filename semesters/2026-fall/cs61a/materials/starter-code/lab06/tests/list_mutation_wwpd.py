from pytest_grader import points


@points(0)
def list_mutation_wwpd():
    """What Would Python Display?

    >>> s = [6, 7, 8]
    >>> s.append(6)
    >>> s
    LOCKED: 05a752632ede6070
    >>> s.insert(0, 9)
    >>> s
    LOCKED: 8057a8ea560b7092
    >>> x = s.pop(1)
    >>> s
    LOCKED: 97ec4206fe797fa5
    >>> s.remove(x)
    >>> s
    LOCKED: f2e40a24ea242fde
    >>> a, b = s, s[:]
    >>> a is s
    LOCKED: d25d80798932633c
    >>> b == s
    LOCKED: 413c31349b5fbc37
    >>> b is s
    LOCKED: e0b3a713c5c62cf6
    >>> a.pop()
    LOCKED: 887c79c9cb99a889
    >>> a + b
    LOCKED: 63e7e3ac898292c8
    >>> s = [3]
    >>> s.extend([4, 5])
    >>> s
    LOCKED: fc4b90a5fd76ed4e
    >>> a
    LOCKED: a789c0fd82e0b497
    >>> s.extend([s.append(9), s.append(10)])
    >>> s
    LOCKED: 3c297769ab18496c
    """
