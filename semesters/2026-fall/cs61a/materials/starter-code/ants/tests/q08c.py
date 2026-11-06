from pytest_grader import points


@points(0)
def problem_08c_check():
    r"""
    >>> from ants import *
    >>> # Testing ProtectorAnt parameters
    >>> protector = ProtectorAnt()
    >>> ProtectorAnt.food_cost
    LOCKED: c069f6c8e23fcbef
    >>> protector.health
    LOCKED: 08b710b84855519c
    """


@points(1)
def problem_08c():
    r"""
    >>> from ants import *
    >>> # Abstraction tests
    >>> original = ContainerAnt.__init__
    >>> ContainerAnt.__init__ = lambda self, health: print("init") #If this errors, you are not calling the parent constructor correctly.
    >>> protector = ProtectorAnt()
    init
    >>> ContainerAnt.__init__ = original
    >>> protector = ProtectorAnt()
    >>> hasattr(protector, 'ant_contained')
    True
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> gamestate = GameState(beehive, ant_types(), layout, (1, 9))
    >>> #
    >>> protector = ProtectorAnt()
    >>> protector.action(gamestate) # Action without contained ant should not error
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> gamestate = GameState(beehive, ant_types(), layout, (1, 9))
    >>> #
    >>> # Testing protector performs thrower's action
    >>> protector = ProtectorAnt()
    >>> thrower = ThrowerAnt()
    >>> bee = Bee(2)
    >>> # Place protector before thrower
    >>> gamestate.places["tunnel_0_0"].add_insect(protector)
    >>> gamestate.places["tunnel_0_0"].add_insect(thrower)
    >>> gamestate.places["tunnel_0_3"].add_insect(bee)
    >>> protector.action(gamestate)
    >>> bee.health
    1
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> gamestate = GameState(beehive, ant_types(), layout, (1, 9))
    >>> #
    >>> # Testing protector performs thrower's action
    >>> protector = ProtectorAnt()
    >>> thrower = ThrowerAnt()
    >>> bee = Bee(2)
    >>> # Place thrower before protector
    >>> gamestate.places["tunnel_0_0"].add_insect(thrower)
    >>> gamestate.places["tunnel_0_0"].add_insect(protector)
    >>> gamestate.places["tunnel_0_3"].add_insect(bee)
    >>> protector.action(gamestate)
    >>> bee.health
    1
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> gamestate = GameState(beehive, ant_types(), layout, (1, 9))
    >>> #
    >>> # Testing removing a protector doesn't remove contained ant
    >>> place = gamestate.places['tunnel_0_0']
    >>> protector = ProtectorAnt()
    >>> test_ant = Ant(1)
    >>> # add protector first
    >>> place.add_insect(protector)
    >>> place.add_insect(test_ant)
    >>> gamestate.remove_ant('tunnel_0_0')
    >>> place.ant is test_ant
    True
    >>> protector.place is None
    True
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> gamestate = GameState(beehive, ant_types(), layout, (1, 9))
    >>> #
    >>> # Testing removing a protector doesn't remove contained ant
    >>> place = gamestate.places['tunnel_0_0']
    >>> protector = ProtectorAnt()
    >>> test_ant = Ant(1)
    >>> # add ant first
    >>> place.add_insect(test_ant)
    >>> place.add_insect(protector)
    >>> gamestate.remove_ant('tunnel_0_0')
    >>> place.ant is test_ant
    True
    >>> protector.place is None
    True
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> gamestate = GameState(beehive, ant_types(), layout, (1, 9))
    >>> #
    >>> # Testing protectored ant keeps instance attributes
    >>> test_ant = Ant()
    >>> def new_action(gamestate):
    ...     test_ant.health += 9000
    >>> test_ant.action = new_action
    >>> place = gamestate.places['tunnel_0_0']
    >>> protector = ProtectorAnt()
    >>> place.add_insect(test_ant)
    >>> place.add_insect(protector)
    >>> place.ant.action(gamestate)
    >>> place.ant.ant_contained.health
    9001
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> gamestate = GameState(beehive, ant_types(), layout, (1, 9))
    >>> #
    >>> # Testing single ProtectorAnt cannot hold two other ants
    >>> protector = ProtectorAnt()
    >>> first_ant = ThrowerAnt()
    >>> place = gamestate.places['tunnel_0_0']
    >>> place.add_insect(protector)
    >>> place.add_insect(first_ant)
    >>> second_ant = ThrowerAnt()
    >>> place.add_insect(second_ant)
    Traceback (most recent call last):
    ...
    AssertionError: Too many ants in tunnel_0_0
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> gamestate = GameState(beehive, ant_types(), layout, (1, 9))
    >>> #
    >>> # Testing ProtectorAnt cannot hold another ProtectorAnt
    >>> protector1 = ProtectorAnt()
    >>> protector2 = ProtectorAnt()
    >>> place = gamestate.places['tunnel_0_0']
    >>> place.add_insect(protector1)
    >>> place.add_insect(protector2)
    Traceback (most recent call last):
    ...
    AssertionError: Too many ants in tunnel_0_0
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> gamestate = GameState(beehive, ant_types(), layout, (1, 9))
    >>> #
    >>> # Testing ProtectorAnt takes all the damage
    >>> thrower = ThrowerAnt()
    >>> protector = ProtectorAnt()
    >>> bee = Bee(1)
    >>> place = gamestate.places['tunnel_0_0']
    >>> place.add_insect(thrower)
    >>> place.add_insect(protector)
    >>> place.add_insect(bee)
    >>> protector.health
    2
    >>> bee.action(gamestate)
    >>> (protector.health, thrower.health)
    (1, 1)
    >>> bee.action(gamestate)
    >>> (protector.health, thrower.health)
    (0, 1)
    >>> protector.place is None
    True
    >>> place.ant is thrower
    True
    >>> bee.action(gamestate)
    >>> thrower.health
    0
    >>> place.ant is None
    True
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> gamestate = GameState(beehive, ant_types(), layout, (1, 9))
    >>> #
    >>> # test proper call to zero-health callback
    >>> original_zero_health_callback = Insect.zero_health_callback
    >>> Insect.zero_health_callback = lambda x: print("insect died")
    >>> place = gamestate.places["tunnel_0_0"]
    >>> bee = Bee(3)
    >>> protector = ProtectorAnt()
    >>> ant = ThrowerAnt()
    >>> place.add_insect(bee)
    >>> place.add_insect(ant)
    >>> place.add_insect(protector)
    >>> bee.action(gamestate)
    >>> bee.action(gamestate)
    insect died
    >>> bee.action(gamestate) # if you fail this test you probably didn't correctly call Ant.reduce_health or Insect.reduce_health
    insect died
    >>> Insect.zero_health_callback = original_zero_health_callback
    >>> from ants import *
    >>> ProtectorAnt.implemented
    True
    """
