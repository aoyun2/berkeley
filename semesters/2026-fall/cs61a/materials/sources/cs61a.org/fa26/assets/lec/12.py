def reverseA(s):
    """Return s in reverse order.

    >>> reverseA([4, 6, 2])
    [2, 6, 4]
    """
    if not s:
        return []
    reverseA(s[1:] + [s[0]])

def reverseB(s):
    """Return s in reverse order.

    >>> reverseB([4, 6, 2])
    [2, 6, 4]
    """
    if not s:
        return []
    return [s[-1]] + reverseB(s[:-1])

def reverseC(s):
    """Return s in reverse order.

    >>> reverseC([4, 6, 2])
    [2, 6, 4]
    """
    if not s:
        return []
    return [s[-1 * i] for i in range(len(s))]

def reverseD(s: list[int]) -> list[int]:
    """Return s in reverse order.

    >>> reverseD([4, 6, 2])
    [2, 6, 4]
    """
    if not s:
        return []
    return [s[-x + 1] for x in range(reverseD(s))]









def double_eights1(s):
    """Return whether two consecutive items 
    of list s are 8.

    >>> double_eights1([1, 2, 8, 8])
    True
    >>> double_eights1([8, 8, 0])
    True
    >>> double_eights1([5, 3, 8, 8, 3, 5])
    True
    >>> double_eights1([2, 8, 4, 6, 8, 2])
    False
    """
    for i in range(len(s) - 1):
        #if s[i] == 8 and s[i + 1] == 8:
        if s[i] == 8 and s[i + 1] == 8:
            return True
    return False

def double_eights2(s):
    """Return whether two consecutive items 
    of list s are 8.

    >>> double_eights2([1, 2, 8, 8])
    True
    >>> double_eights2([8, 8, 0])
    True
    >>> double_eights2([5, 3, 8, 8, 3, 5])
    True
    >>> double_eights2([2, 8, 4, 6, 8, 2])
    False
    """
    for i in range(len(s) - 1):
        if s[i] == 8 and s[i + 1] == 8:
            return True
    return False

def cube(k):
    return pow(k, 3)

def summation(n, term):
    """Sum the first n terms of a sequence.

    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def summation2(n, term):
    return sum([term(x) for x in range(1, n + 1)])

min(range(10), key=lambda i: abs(50 ** 0.5 - i))
sum([2, 3, 4], sum([20, 30, 40]))
any([x > 10 for x in range(10)])

def str_example():
    """
    >>> s = '3 * '
    >>> print(s + s + s + 10)
    Traceback (most recent call last):
        ... 
    TypeError: can only concatenate str (not "int") to str
    >>> print(s + s + s + str(10))
    3 * 3 * 3 * 10
    >>> eval(s + s + s + str(10))
    270
    """