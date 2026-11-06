def demo1():
    """
    >>> x = 6
    >>> digits = [1, 8, 0, 8]
    >>> digits
    [1, 8, 0, 8]
    >>> digits[2] # Get one element out of the list. List indices start at 0!
    0
    >>> def get_index():
    ...   return 1
    ...
    >>> digits[get_index()]
    8
    >>> def get_list(n):
    ...   return [n, n + 1, n + 2]
    ...
    >>> get_list(3)
    [3, 4, 5]
    >>> get_list(3)[get_index()]
    4
    >>> 1 in digits
    True
    >>> 2 in digits
    False
    >>> [1, 8] in digits
    False
    >>> other_digits = [1, 2, [1, 8]]
    >>> [1, 8] in other_digits
    True
    >>> digits + other_digits
    [1, 8, 0, 8, 1, 2, [1, 8]]
    >>> len(digits)
    4
    >>> type(digits)
    <class 'list'>
    >>> digits2: list[int] = [1, 4, 5]
    """
    return

def demo2():
    """
    >>> digits = [1, 8, 0, 8]
    >>> i = 0
    >>> while i < len(digits):
    ...   print(digits[i])
    ...   i += 1
    ...
    1
    8
    0
    8
    >>> for d in digits:
    ...   print(d)
    ...
    1
    8
    0
    8
    """
    return

def range_demo():
    """
    >>> range(3)
    range(0, 3)
    >>> for x in range(3):
    ...   print(x)
    ...
    0
    1
    2
    >>> digits = [1, 0, 1, 8]
    >>> for i in range(len(digits)):
    ...   print(digits[i])
    ...
    1
    0
    1
    8
    >>> [100 * d for d in digits]
    [100, 0, 100, 800]
    >>> [100 * d for d in digits if d < 5]
    [100, 0, 100]
    """
    return