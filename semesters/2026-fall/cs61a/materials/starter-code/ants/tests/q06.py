from pytest_grader import points


@points(1)
def problem_06():
    r"""
    >>> from ants import *
    >>> # Testing WallAnt parameters
    >>> wall = WallAnt()
    >>> wall.name
    'Wall'
    >>> wall.health
    4
    >>> # `health` should not be a class attribute
    >>> not hasattr(WallAnt, 'health') # hasattr checks if the WallAnt class has a class attribute called 'health'
    True
    >>> WallAnt.food_cost
    4
    >>> # Abstraction tests
    >>> original = Ant.__init__
    >>> Ant.__init__ = lambda self, health: print("init") #If this errors, you are not calling the parent constructor correctly.
    >>> wall = WallAnt()
    init
    >>> Ant.__init__ = original
    >>> wall = WallAnt()
    >>> # Testing WallAnt holds strong
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> gamestate = GameState(beehive, ant_types(), layout, (1, 9))
    >>> place = gamestate.places['tunnel_0_4']
    >>> wall = WallAnt()
    >>> bee = Bee(1000)
    >>> place.add_insect(wall)
    >>> place.add_insect(bee)
    >>> for i in range(3):
    ...     bee.action(gamestate)
    ...     wall.action(gamestate)   # WallAnt does nothing
    >>> wall.health
    1
    >>> bee.health
    1000
    >>> wall.place is place
    True
    >>> bee.place is place
    True
    >>> from ants import *
    >>> WallAnt.implemented
    True
    """
