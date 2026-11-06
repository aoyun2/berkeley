def ten_pairs_syntax_check():
    """Check that ten_pairs uses recursion, not loops.

    >>> from lab03 import ten_pairs
    >>> # This test checks that you used recursion, with no loops.
    >>> import inspect, ast
    >>> tree = ast.parse(inspect.getsource(ten_pairs))
    >>> [type(x).__name__ for x in ast.walk(tree) if type(x).__name__ in ['For', 'While']]
    []
    """
