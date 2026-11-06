def double_eights_syntax_check():
    """Check that double_eights uses recursion, not loops, `in`, or `str`.

    >>> from lab03 import double_eights
    >>> # This test checks that you used recursion, with no loops or `in`.
    >>> import inspect, ast
    >>> tree = ast.parse(inspect.getsource(double_eights))
    >>> banned = ['For', 'While', 'In', 'JoinedStr']
    >>> [type(x).__name__ for x in ast.walk(tree) if type(x).__name__ in banned]
    []
    >>> # This test checks that you did not call the str function.
    >>> [x.id for x in ast.walk(tree) if type(x).__name__ == 'Name' and x.id == 'str']
    []
    """
