from pytest_grader import points


@points(0)
def problem_05_check():
    r"""
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing FireAnt parameters
    >>> fire = FireAnt()
    >>> FireAnt.food_cost
    LOCKED: 08cc243c03247ac1
    >>> fire.health
    LOCKED: fb6b6feabe64c646
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing fire does damage to all Bees in its Place
    >>> place = gamestate.places['tunnel_0_4']
    >>> fire = FireAnt(health=1)
    >>> place.add_insect(fire)        # Add a FireAnt with 1 health
    >>> place.add_insect(Bee(3))      # Add a Bee with 3 health
    >>> place.add_insect(Bee(5))      # Add a Bee with 5 health
    >>> len(place.bees)               # How many bees are there?
    LOCKED: 422b810f37647117
    >>> place.bees[0].action(gamestate)  # The first Bee attacks FireAnt
    >>> fire.health
    LOCKED: e526192c16603957
    >>> fire.place is None
    LOCKED: 8e9db03461824bab
    >>> len(place.bees)               # How many bees are left?
    LOCKED: d331a5a1bc95fdc0
    >>> place.bees[0].health           # What is the health of the remaining Bee?
    LOCKED: 648e5eeb43342f81
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> place = gamestate.places['tunnel_0_4']
    >>> ant = FireAnt(health=1)           # Create a FireAnt with 1 health
    >>> place.add_insect(ant)      # Add a FireAnt to place
    >>> ant.place is place
    LOCKED: 6ded55daf64e9513
    >>> place.remove_insect(ant)   # Remove FireAnt from place
    >>> ant.place is place         # Is the ant's place still that place?
    LOCKED: efa0db9d7848deb7
    """


@points(3)
def problem_05():
    r"""
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Abstraction tests
    >>> original = Ant.__init__
    >>> Ant.__init__ = lambda self, health: print("init") #If this errors, you are not calling the parent constructor correctly.
    >>> fire = FireAnt()
    init
    >>> Ant.__init__ = original
    >>> fire = FireAnt()
    >>> original = Ant.reduce_health
    >>> Ant.reduce_health = lambda self, amount: print("reduced") #If this errors, you are not calling the inherited method correctly
    >>> place = gamestate.places['tunnel_0_4']
    >>> place.add_insect(fire)
    >>> fire.reduce_health(1)
    reduced
    >>> Ant.reduce_health = original
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing fire damage when the fire ant does not die
    >>> place = gamestate.places['tunnel_0_4']
    >>> bee = Bee(5)
    >>> ant = FireAnt(health=100)
    >>> place.add_insect(bee)
    >>> place.add_insect(ant)
    >>> bee.action(gamestate) # attack the FireAnt
    >>> ant.health
    99
    >>> bee.health
    4
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing no hardcoded 3
    >>> place = gamestate.places['tunnel_0_4']
    >>> bee = Bee(100)
    >>> ant = FireAnt(health=1)
    >>> ant.damage = 49
    >>> place.add_insect(bee)
    >>> place.add_insect(ant)
    >>> bee.action(gamestate) # attack the FireAnt
    >>> ant.health
    0
    >>> bee.health
    50
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing fire damage when the fire ant does die
    >>> place = gamestate.places['tunnel_0_4']
    >>> bee = Bee(5)
    >>> ant = FireAnt(health=1)
    >>> place.add_insect(bee)
    >>> place.add_insect(ant)
    >>> bee.action(gamestate) # attack the FireAnt
    >>> ant.health
    0
    >>> bee.health
    1
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing fire does damage to all Bees in its Place
    >>> place = gamestate.places['tunnel_0_4']
    >>> place.add_insect(FireAnt(1))
    >>> for i in range(100):          # Add 100 Bees with 3 health
    ...     place.add_insect(Bee(3))
    >>> place.bees[0].action(gamestate)  # The first Bee attacks FireAnt
    >>> len(place.bees)               # How many bees are left?
    0
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing fire damage is instance attribute
    >>> place = gamestate.places['tunnel_0_4']
    >>> bee = Bee(900)
    >>> buffAnt = FireAnt(1)
    >>> buffAnt.damage = 500   # Feel the burn!
    >>> place.add_insect(bee)
    >>> place.add_insect(buffAnt)
    >>> bee.action(gamestate) # attack the FireAnt
    >>> bee.health  # is damage an instance attribute?
    399
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # General FireAnt Test
    >>> place = gamestate.places['tunnel_0_4']
    >>> bee = Bee(10)
    >>> ant = FireAnt(1)
    >>> place.add_insect(bee)
    >>> place.add_insect(ant)
    >>> bee.action(gamestate)    # Attack the FireAnt
    >>> bee.health
    6
    >>> ant.health
    0
    >>> place.ant is None     # The FireAnt should not occupy the place anymore
    True
    >>> bee.action(gamestate)
    >>> bee.health             # Bee should not get damaged again
    6
    >>> bee.place.name        # Bee should not have been blocked
    'tunnel_0_3'
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # General FireAnt Test
    >>> place = gamestate.places['tunnel_0_4']
    >>> bee = Bee(10)
    >>> ant = FireAnt()
    >>> place.add_insect(bee)
    >>> place.add_insect(ant)
    >>> ant.reduce_health(0.1) # Poke the FireAnt
    >>> bee.health             # Bee should only get slightly damaged
    9.9
    >>> ant.health
    2.9
    >>> place.ant is ant      # The FireAnt should still be at place
    True
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # test proper call to zero-health callback
    >>> original_zero_health_callback = Insect.zero_health_callback
    >>> Insect.zero_health_callback = lambda x: print("insect died")
    >>> place = gamestate.places["tunnel_0_0"]
    >>> bee = Bee(3)
    >>> ant = FireAnt()
    >>> place.add_insect(bee)
    >>> place.add_insect(ant)
    >>> bee.action(gamestate)
    >>> bee.action(gamestate)
    >>> bee.action(gamestate) # if you fail this test you probably didn't correctly call Ant.reduce_health or Insect.reduce_health
    insect died
    insect died
    >>> Insect.zero_health_callback = original_zero_health_callback
    >>> from ants import *
    >>> FireAnt.implemented
    True
    """
