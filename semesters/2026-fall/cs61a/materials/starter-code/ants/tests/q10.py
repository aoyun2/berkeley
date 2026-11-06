from pytest_grader import points


@points(0)
def problem_10_check():
    r"""
    >>> from ants import *
    >>> from ants_plans import *
    >>> beehive, layout = Hive(make_test_assault_plan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing water with soggy (non-waterproof) bees
    >>> test_bee = Bee(1000000)
    >>> test_bee.is_waterproof = False    # Make Bee non-waterproof
    >>> test_water = Water('Water Test2')
    >>> test_water.add_insect(test_bee)
    >>> test_bee.health
    LOCKED: 37fa9de81944bcbd
    >>> len(test_water.bees)
    LOCKED: 871f2e14404cecfe
    >>> # Testing water with waterproof bees
    >>> test_bee = Bee(1)
    >>> test_water = Water('Water Test3')
    >>> test_water.add_insect(test_bee)
    >>> test_bee.health
    LOCKED: 7469cfa406ee3771
    >>> test_bee in test_water.bees
    LOCKED: 371362072769ce8b
    """


@points(1)
def problem_10():
    r"""
    >>> from ants import *
    >>> from ants_plans import *
    >>> beehive, layout = Hive(make_test_assault_plan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing water with Ants
    >>> test_water = Water('Water Test1')
    >>> ant = HarvesterAnt()
    >>> test_water.add_insect(ant)
    >>> (ant.health, test_water.ant is None)
    (0, True)
    >>> ant = Ant()
    >>> test_water.add_insect(ant)
    >>> (ant.health, test_water.ant is None)
    (0, True)
    >>> ant = ThrowerAnt()
    >>> test_water.add_insect(ant)
    >>> (ant.health, test_water.ant is None)
    (0, True)
    >>> # test proper call to zero-health callback
    >>> original_zero_health_callback = Insect.zero_health_callback
    >>> Insect.zero_health_callback = lambda x: print("insect died")
    >>> place = Water('Water Test4')
    >>> soggy_bee = Bee(1)
    >>> soggy_bee.is_waterproof = False
    >>> place.add_insect(soggy_bee)
    insect died
    >>> place.add_insect(Bee(1))
    >>> place.add_insect(ThrowerAnt())
    insect died
    >>> Insect.zero_health_callback = original_zero_health_callback
    >>> from ants import *
    >>> from ants_plans import *
    >>> beehive, layout = Hive(make_test_assault_plan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> old_add_insect = Place.add_insect
    >>> # Testing water inheritance
    >>> old_add_insect = Place.add_insect
    >>> def new_add_insect(self, insect):
    ...     print("called add_insect")
    ...     old_add_insect(self, insect)
    >>> Place.add_insect = new_add_insect
    >>> test_bee = Bee(1)
    >>> test_water = Water('Water Test4')
    >>> test_water.add_insect(test_bee) # if this fails you probably didn't call `add_insect`
    called add_insect
    >>> Place.add_insect = old_add_insect
    """
