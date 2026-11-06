from __future__ import annotations
from dataclasses import dataclass, field

def prefixes(s):
    """Return a list of all of the list prefixes of s, including s.
    
    >>> prefixes([1, 2, 3])
    [[1], [1, 2], [1, 2, 3]
    """
    so_far = []
    result = []
    for x in s:
        so_far.append(x)
        result.append(so_far)
        # Fixed version: result.append(list(so_far))
    return result

@dataclass
class Tree[T]:
    label: T
    branches: list[Tree[T]] = field(default_factory=list)  # branches defaults to []

    def __str__(self):
        return format_tree(self)

def format_tree(t: Tree, indent='') -> str:
    "Format a tree with each branch indented below its label."
    assert isinstance(t, Tree), f'{t!r} is not a Tree'
    assert isinstance(t.branches, list), f'branches of {t!r} is not a list'
    string = indent + str(t.label)
    for b in t.branches:
        string += '\n' + format_tree(b, indent + '  ')
    return string

def is_leaf(t: Tree) -> bool:
    "Return whether a Tree t is a leaf with no branches."
    return not t.branches

def exclude(t, x):
    """Return a tree with the non-root nodes of tree t labeled anything but x.

    >>> t = Tree(1, [Tree(2, [Tree(2), Tree(3), Tree(4)]), Tree(5, [Tree(1)])])
    >>> print(exclude(t, 2))
    1
      3
      4
      5
        1
    """
    filtered_branches = map(lambda y: exclude(y, x), t.branches)
    bs = []
    for b in filtered_branches:
        if b.label == x:
            bs.extend(b.branches)
        else:
            bs.append(b)
    return Tree(t.label, bs)

def display(fruit: str, count: int) -> str:
    """Display a count of a fruit in angle brackets.

    >>> display('apples', 3)
    '<3 apples>'
    >>> display('apples', 1)
    '<1 apple>'
    >>> display('kiwis', 12)
    '<12 kiwis>'
    >>> print(display('apples', 3) + display('kiwis', 3))
    <3 apples><3 kiwis>
    """
    assert count >= 1 and fruit[-1] == 's'
    if count == 1:
        return f'<{count} {fruit[:-1]}>'
    return f'<{count} {fruit}>'

def buy(fruits_to_buy: list[str], prices: dict[str, int], total_amount: int) -> None:
    """Print ways to buy some of each fruit so that the sum of prices is amount.

    >>> prices = {'oranges': 4, 'apples': 3, 'bananas': 2, 'kiwis': 9}
    >>> buy(['apples', 'oranges', 'bananas'], prices, 12)  # We can only buy apple, orange, and banana, but not kiwi
    <2 apples><1 orange><1 banana>
    >>> buy(['apples', 'oranges', 'bananas'], prices, 16)
    <2 apples><1 orange><3 bananas>
    <2 apples><2 oranges><1 banana>
    >>> buy(['apples', 'kiwis'], prices, 36)
    <3 apples><3 kiwis>
    <6 apples><2 kiwis>
    <9 apples><1 kiwi>
    """
    def add(fruits: list[str], amount: int, cart: str) -> None:
        if fruits == [] and amount == 0:
            print(cart)
        elif fruits and amount > 0:
            fruit = fruits[0]
            price = prices[fruit]
            for k in range(1, amount // price + 1):
                # Hint: The display function will help you add fruit to the cart.
                add(fruits[1:], amount - price * k, cart + display(fruit, k))
    add(fruits_to_buy, total_amount, '')

def all_elements(t: Tree):
    """
    >>> t = Tree('o', [Tree('a'), Tree('W', [Tree('o'), Tree('a', [Tree('d'), Tree('l')])])])
    >>> all = all_elements(t)
    >>> next(all)
    'a'
    >>> # Write an expression that evaluates to ['W', 'a', 'l', 'd', 'o']
    >>> list(reversed(list(all)[:-1]))
    ['W', 'a', 'l', 'd', 'o']
    """
    for b in t.branches:
        yield from all_elements(b)
    yield t.label