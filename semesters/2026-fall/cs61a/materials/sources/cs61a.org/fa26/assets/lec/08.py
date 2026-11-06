def square(x):
    """Square x.

    >>> square(3)
    9
    """
    return pow(x, 2)

def cube(x):
    """Cube x.

    >>> cube(3)
    27
    """
    return pow(x, 3)

def reverse(f):
    return lambda x, y: f(y, x)

def curry(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

square = _______________