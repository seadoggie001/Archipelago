import dataclasses

from ..Data.Item import ItemNames
from ..Data.Region import RegionNames
from ..Data.Rules import RuleNames, Requirement
from ..Data.Resources import Resources


@dataclasses.dataclass
class Statistic:
    key: str
    value: str


@dataclasses.dataclass
class TimedStatistic:
    key: str
    value: str
    time: str


@dataclasses.dataclass
class LocationData:
    id: int
    name: str
    description: str
    region: str
    '''Name of the region'''
    requirements: list[Requirement | str] | None = None
    '''List of required items'''
    achievement: str | None = None
    '''Internal game achievement name'''
    statistic: Statistic | None = None
    '''Statistic used to determine how the location is granted'''
    timed: TimedStatistic | None = None
    '''A Statistic that must be completed in a set amount of time'''
    option: str | None = None

class Options:
    GrassSanity="Grass Sanity"


def add_grass_sanity() -> list[LocationData]:
    i:int = 23000
    locs:list[LocationData] = []
    for x in range(0, 32):
        for y in range(0, 32):
            loc = LocationData(
                i,
                name=f"Grass ({x}, {y})",
                description=f"Harvest hay at ({x}, {y})",
                region=RegionNames.Grass,
                option=Options.GrassSanity,
            )
            locs.append(add_requirements(loc, x, y))
            i += 1
    return locs

def add_requirements(loc: LocationData, x:int, y:int) -> LocationData:
    if x == 0 and y == 0:
        pass
    elif x == 0 and y < 3:
        loc.requirements = [ItemNames.Expand]
    elif x < 3 and y < 3:
        loc.requirements = [Requirement(ItemNames.Expand, 2)]
    elif x < 4 and y < 4:
        loc.requirements = [Requirement(ItemNames.Expand, 3)]
    elif x < 6 and y < 6:
        loc.requirements = [Requirement(ItemNames.Expand, 4)]
    elif x < 8 and y < 8:
        loc.requirements = [Requirement(ItemNames.Expand, 5)]
    elif x < 12 and y < 12:
        loc.requirements = [Requirement(ItemNames.Expand, 6)]
    elif x < 16 and y < 16:
        loc.requirements = [Requirement(ItemNames.Expand, 7)]
    elif x < 22 and y < 22:
        loc.requirements = [Requirement(ItemNames.Expand, 8)]
    else:
        loc.requirements = [Requirement(ItemNames.Expand, 9)]
    return loc


# Location identifiers start at 10K and are grouped by categories into their own 1K ids. "Categories" are not regions.
ALL_LOCATION_DATA: list[LocationData] = [
    # region 10Ks Not crop related
    LocationData(
        10000,
        name="Hello World!",
        description="Run your first code",
        region=RegionNames.Start,
        achievement="RUN_YOUR_FIRST_CODE"
    ),
    LocationData(
        10001,
        name="Ouroboros",
        description="Create an infinite loop",
        region=RegionNames.Start,
        achievement="INFINITE_LOOP",
        requirements=[ItemNames.Loop],
    ),
    LocationData(
        10002,
        name="It's ALIVE!",
        description="Expand the farm",
        region=RegionNames.Start,
        achievement="EXPAND",
        requirements=[ItemNames.Expand]
    ),
    LocationData(
        10003,
        name="Error 404 - Achievement not found",
        description="Cause a runtime error",
        region=RegionNames.Start,
        achievement="CAUSE_A_RUNTIME_ERROR"
    ),
    LocationData(
        10004,
        name="Not quite bacon...",
        description="Pet the piggy",
        region=RegionNames.Start,
        achievement="PET_THE_PIGGY"
    ),
    LocationData(
        10005,
        name="func(func(func(func(func))))",
        description="Pass a function to a function",
        region=RegionNames.Start,
        achievement="HIGHER_ORDER_PROGRAMMING",
        requirements=[ItemNames.Functions]
    ),
    LocationData(
        10006,
        name="What are you doing in my swamp!?",
        description="Make the entire farm have a water level > 0.5",
        region=RegionNames.Start,
        achievement="MUD_FARM",
        requirements=[ItemNames.Watering]
    ),
    LocationData(
        10007,
        name="Treasure Hunter",
        description="Solve a maze that fills the whole farm",
        region=RegionNames.Maze,
        achievement="TREASURE_HUNTER"
    ),
    LocationData(
        10008,
        name="Parallel Processing",
        description="Use multiple drones",
        region=RegionNames.Drones,
        achievement="USE_MULTIPLE_DRONES"
    ),
    LocationData(
        10009,
        name="Fashionable",
        description="Wear a hat",
        region=RegionNames.Start,
        achievement="EQUIP_A_NEW_HAT",
        requirements=[RuleNames.AnyHatItems],
    ),
    LocationData(
        10010,
        name="Ancient Lizard Hat",
        description="Equip the dinosaur hat",
        region=RegionNames.Dinos,
        achievement="EQUIP_DINO_HAT",
    ),
    LocationData(
        10011,
        name="Healer",
        description="Heal an infected plant",
        region=RegionNames.WeirdSubstance,
        achievement="HEALER",
    ),
    LocationData(
        10012,
        name="Big Farm",
        description="Reach the maximum farm size",
        region=RegionNames.Start,
        achievement="BIG_FARM",
        requirements=[
            RuleNames.ReallyBigFarm
        ],
    ),
    LocationData(
        10013,
        name="Chaos",
        description="Open 20 windows at once. You monster.",
        region=RegionNames.Start,
        achievement="CHAOS",
    ),
    LocationData(
        10014,
        name="sutcaC",
        description="Sort a full field of cactus the wrong way round",
        region=RegionNames.Cactus,
        achievement="WRONG_ORDER",
    ),
    LocationData(
        10015,
        name="Patagotitan",
        description="Have a dinosaur that fills the entire farm",
        region=RegionNames.Dinos,
        achievement="LONG_DINOSAUR",
    ),
    LocationData(
        10016,
        name="Swarm",
        description="Have 32 drones at once",
        region=RegionNames.Drones,
        achievement="SWARM",
        requirements=[Requirement(ItemNames.Megafarm, 5)],
    ),
    LocationData(
        10017,
        name="Stack Overflow",
        description="Stack overflow. Not the website.",
        region=RegionNames.Start,
        achievement="STACK_OVERFLOW",
        requirements=[ItemNames.Functions],
    ),
    LocationData(
        10018,
        name="Circular Import",
        description="Import a file from another file that imports from...",
        region=RegionNames.Start,
        achievement="CIRCULAR_IMPORT",
        requirements=[ItemNames.Import],
    ),
    LocationData(
        10019,
        name="Prize Pumpkin",
        description="Harvest a 32x32 pumpkin",
        region=RegionNames.Pumpkins,
        achievement="GIANT_PUMPKIN",
        requirements=[RuleNames.ReallyBigFarm],
    ),
    LocationData(
        10020,
        name="Size Matters",
        description="Get a dinosaur to length 1K",
        region=RegionNames.Dinos,
        achievement="SIZE_MATTERS",
        requirements=[
            Requirement(ItemNames.Expand, 9),
            Requirement(ItemNames.Dinosaurs, 4),
            Requirement(ItemNames.Drone_Speed, 5),
        ],
    ),
    LocationData(
        10021,
        name="Recycling",
        description="Reuse the same maze 300 times",
        region=RegionNames.Maze,
        achievement="RECYCLING",
        requirements=[Requirement(ItemNames.Fertilizer, 3)],
    ),
    LocationData(
        10022,
        name="Fashion Show",
        description="Equip 5 different hats on 5 drones",
        region=RegionNames.Drones,
        achievement="FASHION_SHOW",
        requirements=[
            Requirement(ItemNames.Megafarm, 3),
            ItemNames.Hats
        ],
    ),
    LocationData(
        10023,
        name="Maze",
        description="Spawn a maze",
        region=RegionNames.Maze,
        achievement="SPAWN_MAZE",
    ),
    # endregion
    # region 11Ks Flips
    LocationData(
        11000,
        name="Acrobat",
        description="Do a flip!",
        achievement="DO_A_FLIP",
        region=RegionNames.Flip,
        statistic=Statistic(Resources.Flips, "1")
    ),
    LocationData(
        11001,
        name="10 Flips",
        description="Flip 10 times",
        region=RegionNames.Flip,
        statistic=Statistic(Resources.Flips, "10")
    ),
    LocationData(
        11002,
        name="Flipping Awesome",
        description="Flip 100 times",
        region=RegionNames.Flip,
        statistic=Statistic(Resources.Flips, "100"),
    ),
    LocationData(
        11003,
        name="Getting Dizzy",
        description="Flip 1K times",
        region=RegionNames.Flip,
        statistic=Statistic(Resources.Flips, "1K"),
        requirements=[
            ItemNames.Loop,
            ItemNames.Megafarm,
            ItemNames.Functions,
        ],
    ),
    LocationData(
        11004,
        name="All the flips",
        description="Flip 10K times",
        region=RegionNames.Flip,
        statistic=Statistic(Resources.Flips, "10K"),
        requirements=[
            ItemNames.Loop,
            Requirement(ItemNames.Megafarm, 3),
            ItemNames.Functions,
        ],
    ),
    LocationData(
        11005,
        name="Just keep flipping, just keep flipping",
        description="Flip 100K times",
        region=RegionNames.Flip,
        statistic=Statistic(Resources.Flips, "100K"),
        requirements=[
            ItemNames.Loop,
            Requirement(ItemNames.Megafarm, 5),
            ItemNames.Functions,
        ],
    ),
    # endregion
    # region 12Ks Plant one crop
    LocationData(
        12001,
        name="Bring Me a shrubbery!",
        description="Plant a bush",
        region=RegionNames.Crop,
        achievement="PLANT_BUSH"
    ),
    LocationData(
        12002,
        name="Carrots",
        description="Plant a carrot",
        region=RegionNames.Crop,
        achievement="PLANT_CARROTS",
        requirements=[ItemNames.Carrot],
    ),
    LocationData(
        12003,
        name="Pumpkins",
        description="Plant a pumpkin",
        region=RegionNames.Crop,
        achievement="PLANT_PUMPKIN",
        requirements=[ItemNames.Carrot, ItemNames.Pumpkins],
    ),
    LocationData(
        12004,
        name="Sunflowers",
        description="Plant a sunflower",
        region=RegionNames.Crop,
        achievement="PLANT_SUNFLOWER",
        requirements=[ItemNames.Sunflowers],
    ),
    LocationData(
        12005,
        name="Cactus",
        description="Plant a cactus",
        region=RegionNames.Crop,
        achievement="PLANT_CACTUS",
        requirements=[ItemNames.Carrot, ItemNames.Pumpkins, ItemNames.Cactus],
    ),
    LocationData(
        12006,
        name="Tree",
        description="Plant a tree",
        region=RegionNames.Crop,
        achievement="PLANT_TREE",
        requirements=[ItemNames.Trees]
    ),
    # endregion
    # region 13Ks Hay
    LocationData(
        13000,
        name="10 Hay",
        description="Farm 10 hay",
        region=RegionNames.Hay,
        statistic=Statistic(Resources.Hay, "10"),
    ),
    LocationData(
        13001,
        name="Hay Fever",
        description="Farm 100 hay",
        region=RegionNames.Hay,
        statistic=Statistic(Resources.Hay, "100"),
    ),
    LocationData(
        13002,
        name="Hey, Farmer!",
        description="Farm 1K Hay",
        region=RegionNames.Hay,
        statistic=Statistic(Resources.Hay, "1K"),
        requirements=[
            Requirement(ItemNames.Grass, 2),
            ItemNames.Loop,
        ],
    ),
    LocationData(
        13003,
        name="Cause I have farmed 10K Hay",
        description="Farm 10K hay",
        region=RegionNames.Hay,
        statistic=Statistic(Resources.Hay, "10K"),
        requirements=[
            Requirement(ItemNames.Grass, 3),
            ItemNames.Loop,
            ItemNames.Megafarm,
            ItemNames.Functions,
            ItemNames.Expand,
        ],
    ),
    LocationData(
        13004,
        name="Hay Master",
        description="Farm 100K hay",
        region=RegionNames.Hay,
        statistic=Statistic(Resources.Hay, "100K"),
        requirements=[
            Requirement(ItemNames.Grass, 4),
            ItemNames.Loop,
            Requirement(ItemNames.Megafarm, 2),
            ItemNames.Functions,
            Requirement(ItemNames.Expand, 2),
        ],
    ),
    LocationData(
        13005,
        name="1M Hay",
        description="Farm 1M hay",
        region=RegionNames.Hay,
        statistic=Statistic(Resources.Hay, "1M"),
        requirements=[
            Requirement(ItemNames.Grass, 6),
            ItemNames.Loop,
            Requirement(ItemNames.Megafarm, 3),
            ItemNames.Functions,
            Requirement(ItemNames.Expand, 3),
        ],
    ),
    LocationData(
        13006,
        name="10M Hay",
        description="Farm 10M hay",
        region=RegionNames.Hay,
        statistic=Statistic(Resources.Hay, "10M"),
        requirements=[
            Requirement(ItemNames.Grass, 7),
            ItemNames.Loop,
            Requirement(ItemNames.Megafarm, 3),
            ItemNames.Functions,
            Requirement(ItemNames.Expand, 4),
        ],
    ),
    LocationData(
        13007,
        name="100M Hay",
        description="Farm 100M hay",
        region=RegionNames.Hay,
        statistic=Statistic(Resources.Hay, "100M"),
        requirements=[
            ItemNames.Functions,
            ItemNames.Loop,
            Requirement(ItemNames.Megafarm, 4),
            Requirement(ItemNames.Grass, 8),
            Requirement(ItemNames.Expand, 4),
        ],
    ),
    LocationData(
        13008,
        name="Big Hay Farmer",
        description="Farm 1B hay",
        region=RegionNames.Hay,
        statistic=Statistic(Resources.Hay, "1B"),
        requirements=[
            RuleNames.MaxedOutFarm,
            Requirement(ItemNames.Grass, 10),
        ],
    ),
    # endregion
    # region 15Ks Carrot
    LocationData(
        15000,
        name="10 carrots",
        description="Farm 10 carrots",
        region=RegionNames.Carrot,
        statistic=Statistic(Resources.Carrot, "10"),
    ),
    LocationData(
        15001,
        name="Must be a bunny",
        description="Farm 100 carrots",
        region=RegionNames.Carrot,
        statistic=Statistic(Resources.Carrot, "100"),
        requirements=[
            Requirement(ItemNames.Carrot, 2),
        ]
    ),
    LocationData(
        15002,
        name="Carrot Farmer",
        description="Farm 1K carrots",
        region=RegionNames.Carrot,
        statistic=Statistic(Resources.Carrot, "1K"),
        requirements=[
            Requirement(ItemNames.Carrot, 2),
            Requirement(ItemNames.Expand, 2),
        ],
    ),
    LocationData(
        15003,
        name="10K carrots",
        description="Farm 10K carrots",
        region=RegionNames.Carrot,
        statistic=Statistic(Resources.Carrot, "10K"),
        requirements=[
            Requirement(ItemNames.Carrot, 4),
            Requirement(ItemNames.Expand, 4),
        ],
    ),
    LocationData(
        15004,
        name="100K Carrots",
        description="Farm 100K carrots",
        region=RegionNames.Carrot,
        statistic=Statistic(Resources.Carrot, "100K"),
        requirements=[
            Requirement(ItemNames.Carrot, 5),
            Requirement(ItemNames.Expand, 5),
            ItemNames.Megafarm,
            ItemNames.Functions,
        ],
    ),
    LocationData(
        15005,
        name="All the carrots",
        description="Farm 1M carrots",
        region=RegionNames.Carrot,
        statistic=Statistic(Resources.Carrot, "1M"),
        requirements=[
            Requirement(ItemNames.Carrot, 6),
            Requirement(ItemNames.Expand, 6),
            Requirement(ItemNames.Megafarm, 2),
            ItemNames.Functions,
        ],
    ),
    LocationData(
        15006,
        name="10M Carrots",
        description="Farm 10M carrots",
        region=RegionNames.Carrot,
        statistic=Statistic(Resources.Carrot, "10M"),
        requirements=[
            Requirement(ItemNames.Carrot, 7),
            Requirement(ItemNames.Expand, 7),
            Requirement(ItemNames.Megafarm, 3),
            ItemNames.Functions,
        ],
    ),
    LocationData(
        15007,
        name="100M Carrots",
        description="Farm 100M carrots",
        region=RegionNames.Carrot,
        statistic=Statistic(Resources.Carrot, "100M"),
        requirements=[
            Requirement(ItemNames.Carrot, 8),
            Requirement(ItemNames.Expand, 8),
            Requirement(ItemNames.Megafarm, 3),
            ItemNames.Functions,
        ],
    ),
    LocationData(
        15008,
        name="Orange you glad you're done with carrots?",
        description="Farm 1B carrots",
        region=RegionNames.Carrot,
        statistic=Statistic(Resources.Carrot, "1B"),
        requirements=[
            Requirement(ItemNames.Carrot, 10),
            Requirement(ItemNames.Expand, 9),
            Requirement(ItemNames.Megafarm, 5),
            ItemNames.Functions,
        ],
    ),
    # endregion
    # region 16Ks Wood
    LocationData(
        16000,
        name="10 Wood",
        description="Farm 10 wood",
        region=RegionNames.Wood,
        statistic=Statistic(Resources.Wood, "10"),
    ),
    LocationData(
        16001,
        name="100 Wood",
        description="Farm 100 wood",
        region=RegionNames.Wood,
        statistic=Statistic(Resources.Wood, "100"),
    ),
    LocationData(
        16002,
        name="Deforestation",
        description="Farm 1K Wood",
        region=RegionNames.Wood,
        statistic=Statistic(Resources.Wood, "1K"),
        requirements=[
            ItemNames.Expand,
            ItemNames.Trees
        ],
    ),
    LocationData(
        16003,
        name="10K Wood",
        description="Farm 10K Wood",
        region=RegionNames.Wood,
        statistic=Statistic(Resources.Wood, "10K"),
        requirements=[
            Requirement(ItemNames.Trees, 2),
            Requirement(ItemNames.Expand, 2),
            Requirement(ItemNames.Megafarm, 1),
            ItemNames.Functions,
        ],
    ),
    LocationData(
        16004,
        name="100K Wood",
        description="Farm 100K Wood",
        region=RegionNames.Wood,
        statistic=Statistic(Resources.Wood, "100K"),
        requirements=[
            Requirement(ItemNames.Trees, 3),
            Requirement(ItemNames.Expand, 3),
            Requirement(ItemNames.Megafarm, 2),
            ItemNames.Functions,
        ],
    ),
    LocationData(
        16005,
        name="1M Wood",
        description="Farm 1M Wood",
        region=RegionNames.Wood,
        statistic=Statistic(Resources.Wood, "1M"),
        requirements=[
            Requirement(ItemNames.Trees, 5),
            Requirement(ItemNames.Expand, 5),
            Requirement(ItemNames.Megafarm, 3),
            ItemNames.Functions,
        ],
    ),
    LocationData(
        16006,
        name="10M Wood",
        description="Farm 10M Wood",
        region=RegionNames.Wood,
        statistic=Statistic(Resources.Wood, "10M"),
        requirements=[
            Requirement(ItemNames.Trees, 6),
            Requirement(ItemNames.Expand, 6),
            Requirement(ItemNames.Megafarm, 3),
            ItemNames.Functions,
        ],
    ),
    LocationData(
        16007,
        name="100M Wood",
        description="Farm 100M Wood",
        region=RegionNames.Wood,
        statistic=Statistic(Resources.Wood, "100M"),
        requirements=[
            Requirement(ItemNames.Trees, 8),
            Requirement(ItemNames.Expand, 7),
            Requirement(ItemNames.Megafarm, 4),
            ItemNames.Functions,
        ],
    ),
    LocationData(
        16008,
        name="Big Wood Farmer",
        description="Farm 1B wood",
        region=RegionNames.Wood,
        statistic=Statistic(Resources.Wood, "1B"),
        requirements=[
            Requirement(ItemNames.Trees, 10),
            Requirement(ItemNames.Expand, 9),
            Requirement(ItemNames.Megafarm, 5),
            ItemNames.Functions,
        ],
    ),
    LocationData(
        16009,
        name="Woodn't you know it, you're on the clock",
        description="Farm 1B wood in 1 minute",
        region=RegionNames.Wood,
        timed=TimedStatistic(Resources.Wood, "1B", "1m"),
        requirements=[
            Requirement(ItemNames.Trees, 10),
            RuleNames.MaxedOutFarm
        ]
    ),
    # endregion
    # region 17Ks Pumpkin
    LocationData(
        17000,
        name="10 Pumpkins",
        description="Farm 10 pumpkins",
        region=RegionNames.Pumpkins,
        statistic=Statistic(Resources.Pumpkin, "10"),
    ),
    LocationData(
        17001,
        name="Jack Collector",
        description="Farm 100 pumpkins",
        region=RegionNames.Pumpkins,
        statistic=Statistic(Resources.Pumpkin, "100"),
    ),
    LocationData(
        17002,
        name="1K Pumpkins",
        description="Farm 1K Pumpkins",
        region=RegionNames.Pumpkins,
        statistic=Statistic(Resources.Pumpkin, "1K"),
        requirements=[
            Requirement(ItemNames.Pumpkins, 2),
            Requirement(ItemNames.Expand, 3),
            ItemNames.Drone_Speed,
        ],
    ),
    LocationData(
        17003,
        name="10K Pumpkins",
        description="Farm 10K Pumpkins",
        region=RegionNames.Pumpkins,
        statistic=Statistic(Resources.Pumpkin, "10K"),
        requirements=[
            Requirement(ItemNames.Pumpkins, 3),
            Requirement(ItemNames.Expand, 3),
            ItemNames.Drone_Speed,
        ],
    ),
    LocationData(
        17004,
        name="100K Pumpkins",
        description="Farm 100K Pumpkins",
        region=RegionNames.Pumpkins,
        statistic=Statistic(Resources.Pumpkin, "100K"),
        requirements=[
            Requirement(ItemNames.Pumpkins, 4),
            Requirement(ItemNames.Expand, 3),
            ItemNames.Drone_Speed,
        ],
    ),
    LocationData(
        17005,
        name="1M Pumpkins",
        description="Farm 1M Pumpkins",
        region=RegionNames.Pumpkins,
        statistic=Statistic(Resources.Pumpkin, "1M"),
        requirements=[
            Requirement(ItemNames.Pumpkins, 5),
            Requirement(ItemNames.Expand, 3),
            ItemNames.Drone_Speed,
        ],
    ),
    LocationData(
        17006,
        name="10M Pumpkins",
        description="Farm 10M Pumpkins",
        region=RegionNames.Pumpkins,
        statistic=Statistic(Resources.Pumpkin, "10M"),
        requirements=[
            Requirement(ItemNames.Pumpkins, 6),
            Requirement(ItemNames.Expand, 3),
            ItemNames.Drone_Speed,
        ],
    ),
    LocationData(
        17007,
        name="Big Pumpkin Farmer",
        description="Farm 100M pumpkins",
        region=RegionNames.Pumpkins,
        statistic=Statistic(Resources.Pumpkin, "100M"),
        requirements=[
            Requirement(ItemNames.Pumpkins, 7),
            Requirement(ItemNames.Expand, 4),
            ItemNames.Drone_Speed,
        ],
    ),
    LocationData(
        17008,
        name="Pumpkin Master",
        description="Farm 20M pumpkins in 1 minute",
        region=RegionNames.Pumpkins,
        timed=TimedStatistic(Resources.Pumpkin, "20M", "1m"),
        requirements=[
            Requirement(ItemNames.Pumpkins, 10),
            Requirement(ItemNames.Expand, 4),
            RuleNames.MaxedOutFarm,
        ]
    ),
    # endregion
    # region 18Ks Power
    LocationData(
        18000,
        name="10 Power",
        description="Farm 10 power",
        region=RegionNames.Sunflower,
        statistic=Statistic(Resources.Power, "10"),
    ),
    LocationData(
        18001,
        name="Flower Power",
        description="Farm 100 power",
        region=RegionNames.Sunflower,
        statistic=Statistic(Resources.Power, "100"),
    ),
    LocationData(
        18002,
        name="Power Farmer",
        description="Farm 1K Power",
        region=RegionNames.Sunflower,
        achievement="POWER_FARMER",
        statistic=Statistic(Resources.Power, "1K"),
        requirements=[
            Requirement(ItemNames.Expand, 3),
        ],
    ),
    LocationData(
        18003,
        name="Over 9000!",
        description="Farm 9001 power",
        region=RegionNames.Sunflower,
        statistic=Statistic(Resources.Power, "9001"),
        requirements=[
            Requirement(ItemNames.Expand, 4),
            ItemNames.Megafarm,
            ItemNames.Functions,
        ],
    ),
    LocationData(
        18004,
        name="Unlimited Power Farmer",
        description="Farm 100K Power",
        region=RegionNames.Sunflower,
        statistic=Statistic(Resources.Power, "100K"),
        requirements=[
            Requirement(ItemNames.Expand, 5),
            Requirement(ItemNames.Megafarm, 2),
            ItemNames.Functions,
        ],
    ),
    LocationData(
        18005,
        name="Sunflower Master",
        description="Farm 12K power in 1 minute",
        region=RegionNames.Sunflower,
        timed=TimedStatistic(Resources.Power, "12K", "1m"),
        requirements=[
            RuleNames.MaxedOutFarm,
        ]
    ),
    # endregion
    # region 19Ks Cacti
    LocationData(
        19000,
        name="10 Cacti",
        description="Farm 10 cacti",
        region=RegionNames.Cactus,
        statistic=Statistic(Resources.Cactus, "10")
    ),
    LocationData(
        19001,
        name="A Little Pokey",
        description="Farm 100 cacti",
        region=RegionNames.Cactus,
        statistic=Statistic(Resources.Cactus, "100")
    ),
    LocationData(
        19002,
        name="Can't touch this (ow!)",
        description="Farm 1K Cacti",
        region=RegionNames.Cactus,
        statistic=Statistic(Resources.Cactus, "1K"),
        requirements=[
            Requirement(ItemNames.Expand, 2),
        ]
    ),
    LocationData(
        19003,
        name="10K Cacti",
        description="Farm 10K Cacti",
        region=RegionNames.Cactus,
        statistic=Statistic(Resources.Cactus, "10K"),
        requirements=[
            Requirement(ItemNames.Expand, 4),
        ]
    ),
    LocationData(
        19004,
        name="Kinda Prickly",
        description="Farm 100K cacti",
        region=RegionNames.Cactus,
        statistic=Statistic(Resources.Cactus, "100K"),
        requirements=[
            Requirement(ItemNames.Expand, 5),
        ]
    ),
    LocationData(
        19005,
        name="Big Cactus Farmer",
        description="Farm 1M cacti",
        region=RegionNames.Cactus,
        statistic=Statistic(Resources.Cactus, "1M"),
        requirements=[
            Requirement(ItemNames.Expand, 6),
        ]
    ),
    LocationData(
        19006,
        name="Cactus Master",
        description="Farm 20M cacti in 1 minute",
        region=RegionNames.Cactus,
        timed=TimedStatistic(Resources.Cactus, "20M", "1m"),
        requirements=[
            RuleNames.MaxedOutFarm
        ]
    ),
    # endregion
    # region 20Ks Gold
    LocationData(
        20000,
        name="10 Gold",
        description="Farm 10 Gold",
        region=RegionNames.Maze,
        statistic=Statistic(Resources.Gold, "10")
    ),
    LocationData(
        20001,
        name="Golden Thumb",
        description="Farm 100 Gold",
        region=RegionNames.Maze,
        statistic=Statistic(Resources.Gold, "100")
    ),
    LocationData(
        20002,
        name="Gold Farmer",
        description="Farm 1K Gold",
        region=RegionNames.Maze,
        statistic=Statistic(Resources.Gold, "1K"),
        requirements=[
            ItemNames.Senses,
            ItemNames.Operators,
        ]
    ),
    LocationData(
        20003,
        name="Raking in the Gold",
        description="Farm 10K Gold",
        region=RegionNames.Maze,
        statistic=Statistic(Resources.Gold, "10K"),
        requirements=[
            ItemNames.Senses,
            ItemNames.Operators,
        ]
    ),
    LocationData(
        20004,
        name="All that Glitters",
        description="Farm 100K Gold",
        region=RegionNames.Maze,
        statistic=Statistic(Resources.Gold, "100K"),
        requirements=[
            ItemNames.Senses,
            ItemNames.Operators,
            Requirement(ItemNames.Mazes, 2),
        ]
    ),
    LocationData(
        20005,
        name="Gold Mine",
        description="Farm 1M Gold",
        region=RegionNames.Maze,
        statistic=Statistic(Resources.Gold, "1M"),
        requirements=[
            ItemNames.Senses,
            ItemNames.Operators,
            Requirement(ItemNames.Mazes, 3),
        ]
    ),
    LocationData(
        20006,
        name="10M Gold",
        description="Farm 10M Gold",
        region=RegionNames.Maze,
        statistic=Statistic(Resources.Gold, "10M"),
        requirements=[
            ItemNames.Senses,
            ItemNames.Operators,
            Requirement(ItemNames.Mazes, 4),
        ]
    ),
    LocationData(
        20007,
        name="Going for Gold",
        description="Farm 100M gold",
        region=RegionNames.Maze,
        statistic=Statistic(Resources.Gold, "100M"),
        requirements=[
            ItemNames.Senses,
            ItemNames.Operators,
            Requirement(ItemNames.Mazes, 5),
        ]
    ),
    LocationData(
        20008,
        name="Maze Master",
        description="Farm 2M gold in 1 minute",
        region=RegionNames.Maze,
        timed=TimedStatistic(Resources.Gold, "2M", "1m"),
        requirements=[
            Requirement(ItemNames.Mazes, 5),
            RuleNames.MaxedOutFarm,
        ]
    ),
    # endregion
    # region 21Ks Bones
    LocationData(
        21000,
        name="10 Bones",
        description="Farm 10 Bones",
        region=RegionNames.Dinos,
        statistic=Statistic(Resources.Bone, "10")
    ),
    LocationData(
        21001,
        name="Bone Farmer",
        description="Farm 100 Bones",
        region=RegionNames.Dinos,
        statistic=Statistic(Resources.Bone, "100"),
        requirements=[
            ItemNames.Loop,
        ]
    ),
    LocationData(
        21002,
        name="1K Bones",
        description="Farm 1K Bones",
        region=RegionNames.Dinos,
        statistic=Statistic(Resources.Bone, "1K"),
        requirements=[
            ItemNames.Loop,
        ]
    ),
    LocationData(
        21003,
        name="10K Bones",
        description="Farm 10K Bones",
        region=RegionNames.Dinos,
        statistic=Statistic(Resources.Bone, "10K"),
        requirements=[
            ItemNames.Loop,
            Requirement(ItemNames.Dinosaurs, 2),
            ItemNames.Sunflowers,
        ],
    ),
    LocationData(
        21004,
        name="100K Bones",
        description="Farm 100K Bones",
        region=RegionNames.Dinos,
        statistic=Statistic(Resources.Bone, "100K"),
        requirements=[
            ItemNames.Loop,
            Requirement(ItemNames.Dinosaurs, 3),
            Requirement(ItemNames.Expand, 5),
        ],
    ),
    LocationData(
        21005,
        name="1M Bones",
        description="Farm 1M Bones",
        region=RegionNames.Dinos,
        statistic=Statistic(Resources.Bone, "1M"),
        requirements=[
            ItemNames.Loop,
            Requirement(ItemNames.Dinosaurs, 4),
            Requirement(ItemNames.Expand, 6),
        ],
    ),
    LocationData(
        21006,
        name="10M Bones",
        description="Farm 1M Bones",
        region=RegionNames.Dinos,
        statistic=Statistic(Resources.Bone, "10M"),
        requirements=[
            ItemNames.Loop,
            Requirement(ItemNames.Dinosaurs, 4),
            Requirement(ItemNames.Expand, 7),
        ],
    ),
    LocationData(
        21007,
        name="Big Bone Farmer",
        description="Farm 100M Bones",
        region=RegionNames.Dinos,
        statistic=Statistic(Resources.Bone, "100M"),
        requirements=[
            ItemNames.Loop,
            Requirement(ItemNames.Dinosaurs, 5),
            Requirement(ItemNames.Expand, 8),
        ],
    ),
    LocationData(
        21008,
        name="Dino Master",
        description="Farm 1M bones in 1 minute",
        region=RegionNames.Dinos,
        timed=TimedStatistic(Resources.Bone, "1M", "1m"),
        requirements=[
            ItemNames.Loop,
            Requirement(ItemNames.Dinosaurs, 5),
            RuleNames.MaxedOutFarm,
        ]
    ),
    # endregion
    # region 22Ks Weird Substance
    LocationData(
        22000,
        name="A bit weird",
        description="Farm 1 weird substance",
        region=RegionNames.WeirdSubstance,
        statistic=Statistic(Resources.Weird_Substance, "1"),
    ),
    LocationData(
        22001,
        name="10 Weird Substance",
        description="Farm 10 weird substance",
        region=RegionNames.WeirdSubstance,
        statistic=Statistic(Resources.Weird_Substance, "10"),
    ),
    LocationData(
        22002,
        name="That's kinda weird",
        description="Farm 100 weird substance",
        region=RegionNames.WeirdSubstance,
        statistic=Statistic(Resources.Weird_Substance, "100"),
    ),
    LocationData(
        22003,
        name="That's really weird",
        description="Farm 1K weird substance",
        region=RegionNames.WeirdSubstance,
        statistic=Statistic(Resources.Weird_Substance, "1K"),
        requirements=[
            ItemNames.Megafarm,
            ItemNames.Functions,
            Requirement(ItemNames.Fertilizer, 2),
        ],
    ),
    LocationData(
        22004,
        name="10K Weird Substance",
        description="Farm 10K weird substance",
        region=RegionNames.WeirdSubstance,
        statistic=Statistic(Resources.Weird_Substance, "10K"),
        requirements=[
            Requirement(ItemNames.Megafarm, 2),
            Requirement(ItemNames.Expand, 2),
            Requirement(ItemNames.Fertilizer, 2),
            ItemNames.Functions,
        ],
    ),
    LocationData(
        22005,
        name="100K Weird Substance",
        description="Farm 100K weird substance",
        region=RegionNames.WeirdSubstance,
        statistic=Statistic(Resources.Weird_Substance, "100K"),
        requirements=[
            Requirement(ItemNames.Megafarm, 3),
            Requirement(ItemNames.Expand, 3),
            Requirement(ItemNames.Fertilizer, 3),
            ItemNames.Functions,
        ],
    ),
    # endregion
    #region 23Ks Grass Sanity

    #endregion
    # region 99Ks Timing




    # endregion
] + add_grass_sanity()
"""All location data including names, descriptions, regions, and rules."""
