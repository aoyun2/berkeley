from pytest_grader import points


@points(0)
def problem_02_check():
    r"""
    >>> from ants import *
    >>> from ants_plans import *
    >>> #
    >>> # Create a test layout where the gamestate is a single row with 3 tiles
    >>> beehive, layout = Hive(make_test_assault_plan()), dry_layout
    >>> dimensions = (1, 3)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Simple test for Place
    >>> place0 = Place('place_0')
    >>> print(place0.exit)
    LOCKED: bcbd0c41cdd013ff
    >>> print(place0.entrance)
    LOCKED: cda62960da9e7864
    >>> place1 = Place('place_1', place0)
    >>> place1.exit is place0
    LOCKED: 7200687e29ea8482
    >>> place0.entrance is place1
    LOCKED: 795d044059270862
    """


@points(1)
def problem_02():
    r"""
    >>> from ants import *
    >>> from ants_plans import *
    >>> #
    >>> # Create a test layout where the gamestate is a single row with 3 tiles
    >>> beehive, layout = Hive(make_test_assault_plan()), dry_layout
    >>> dimensions = (1, 3)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing if entrances are properly initialized
    >>> tunnel_len = 9
    >>> len(gamestate.bee_entrances)
    1
    >>> tile_1 = gamestate.bee_entrances[0]
    >>> tile_2 = tile_1.exit
    >>> tile_3 = tile_2.exit
    >>> tile_1.entrance is gamestate.beehive
    True
    >>> tile_1.exit is tile_2
    True
    >>> tile_2.entrance is tile_1
    True
    >>> tile_2.exit is tile_3
    True
    >>> tile_3.entrance is tile_2
    True
    >>> tile_3.exit is gamestate.base
    True
    """
