def count_digit_syntax_check():
    """Check that count_digit uses recursion, not loops.

    >>> from lab03 import count_digit
    >>> # This test checks that you used recursion, with no loops.
    >>> import inspect, ast
    >>> tree = ast.parse(inspect.getsource(count_digit))
    >>> [type(x).__name__ for x in ast.walk(tree) if type(x).__name__ in ['For', 'While']]
    []
    """
