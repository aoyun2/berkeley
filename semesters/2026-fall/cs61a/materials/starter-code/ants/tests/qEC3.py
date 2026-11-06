from pytest_grader import points


@points(0)
def problem_ec3_check():
    r"""
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing NinjaAnt parameters
    >>> ninja = NinjaAnt()
    >>> ninja.health
    LOCKED: acde44698ca72cb1
    >>> NinjaAnt.food_cost
    LOCKED: 5ff25173b7d5a5fc
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing blocks_path
    >>> NinjaAnt.blocks_path
    LOCKED: b8be10ece1fde37f
    >>> HungryAnt.blocks_path
    LOCKED: ebac5aaf7b24546c
    >>> FireAnt.blocks_path
    LOCKED: 1659149929ddf31d
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing NinjaAnts do not block bees
    >>> p0 = gamestate.places["tunnel_0_0"]
    >>> p1 = gamestate.places["tunnel_0_1"]  # p0 is p1's exit
    >>> bee = Bee(2)
    >>> ninja = NinjaAnt()
    >>> thrower = ThrowerAnt()
    >>> p0.add_insect(thrower)            # Add ThrowerAnt to p0
    >>> p1.add_insect(bee)
    >>> p1.add_insect(ninja)              # Add the Bee and NinjaAnt to p1
    >>> bee.action(gamestate)
    >>> bee.place is ninja.place          # Did NinjaAnt block the Bee from moving?
    LOCKED: a8ac91b90b54650a
    >>> bee.place is p0
    LOCKED: 5642d933e4894258
    >>> ninja.health
    LOCKED: 8ad0fecba0a66130
    >>> bee.action(gamestate)
    >>> bee.place is p0                   # Did ThrowerAnt block the Bee from moving?
    LOCKED: 0723b289c11f3784
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing non-blocking ants do not block bees
    >>> p0 = gamestate.places["tunnel_0_0"]
    >>> p1 = gamestate.places["tunnel_0_1"]  # p0 is p1's exit
    >>> bee = Bee(2)
    >>> ninja_fire = FireAnt(1)
    >>> ninja_fire.blocks_path = False
    >>> thrower = ThrowerAnt()
    >>> p0.add_insect(thrower)            # Add ThrowerAnt to p0
    >>> p1.add_insect(bee)
    >>> p1.add_insect(ninja_fire)              # Add the Bee and FireAnt to p1
    >>> bee.action(gamestate)
    >>> bee.place is ninja_fire.place          # Did the "ninjaish" FireAnt block the Bee from moving?
    LOCKED: 618065f8cb4e1e7d
    >>> bee.place is p0
    LOCKED: 3c6a254d9a4e22fa
    >>> ninja_fire.health
    LOCKED: db18eaee4879358f
    >>> bee.action(gamestate)
    >>> bee.place is p0                   # Did ThrowerAnt block the Bee from moving?
    LOCKED: a1cf2e3d33c24e5e
    """


@points(0)
def problem_ec3():
    r"""
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing NinjaAnt strikes all bees in its place
    >>> test_place = gamestate.places["tunnel_0_0"]
    >>> for _ in range(3):
    ...     test_place.add_insect(Bee(2))
    >>> ninja = NinjaAnt()
    >>> test_place.add_insect(ninja)
    >>> ninja.action(gamestate)   # should strike all bees in place
    >>> [bee.health for bee in test_place.bees]
    [1, 1, 1]
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing NinjaAnt doesn't hardcode damage
    >>> test_place = gamestate.places["tunnel_0_0"]
    >>> for _ in range(3):
    ...     test_place.add_insect(Bee(100))
    >>> ninja = NinjaAnt()
    >>> ninja.damage = 50
    >>> test_place.add_insect(ninja)
    >>> ninja.action(gamestate)   # should strike all bees in place
    >>> [bee.health for bee in test_place.bees]
    [50, 50, 50]
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing NinjaAnt strikes all bees, even if some expire
    >>> test_place = gamestate.places["tunnel_0_0"]
    >>> for _ in range(3):
    ...     test_place.add_insect(Bee(1))
    >>> ninja = NinjaAnt()
    >>> test_place.add_insect(ninja)
    >>> ninja.action(gamestate)   # should strike all bees in place
    >>> len(test_place.bees)
    0
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing damage is looked up on the instance
    >>> place = gamestate.places["tunnel_0_0"]
    >>> bee = Bee(900)
    >>> place.add_insect(bee)
    >>> buffNinja = NinjaAnt()
    >>> buffNinja.damage = 500  # Sharpen the sword
    >>> place.add_insect(buffNinja)
    >>> buffNinja.action(gamestate)
    >>> bee.health
    400
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing Ninja ant does not crash when left alone
    >>> ninja = NinjaAnt()
    >>> gamestate.places["tunnel_0_0"].add_insect(ninja)
    >>> ninja.action(gamestate)
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing Bee does not crash when left alone
    >>> bee = Bee(3)
    >>> gamestate.places["tunnel_0_1"].add_insect(bee)
    >>> bee.action(gamestate)
    >>> from ants import *
    >>> NinjaAnt.implemented
    True
    """
