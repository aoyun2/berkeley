def cube(k):
    return pow(k, 3)

common_ratio = 1/2

def get_term(common_ratio):
    def term(k):
        return pow(common_ratio, k)
    return term

common_ratio = 1/3

term = get_term(common_ratio)

def summation(n, term):
    """Sum the first n terms of a sequence.

    >>> summation(5, cube)
    225
    """
    common_ratio = 1/4
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

common_ratio = 1/5
print(summation(5, term))

def curry(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

print(summation(5, curry(pow)(3)))
