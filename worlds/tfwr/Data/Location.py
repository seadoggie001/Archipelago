import dataclasses

from ..Data.Item import ItemNames
from ..Data.Region import RegionNames
from ..Data.Rules import RuleNames, Requirement


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
    '''Statistic used to determine how the location is granted. Should be unused here.'''
    timed: TimedStatistic | None = None
    '''A Statistic that must be completed in a set amount of time'''


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
        region=RegionNames.EndGame,
        achievement="BIG_FARM",
        requirements=[Requirement(ItemNames.Expand,9)],
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
        name="What now",
        description="Unlock the entire game",
        region=RegionNames.EndGame,
        achievement="UNLOCK_EVERYTHING",
        #ToDo: Probably ignore this achievement. It'd require making everything a progression item, I think.
    ),
    LocationData(
        10024,
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
        statistic=Statistic("flips", "1")
    ),
    LocationData(
        11001,
        name="Flipping Awesome",
        description="Flip 100 times",
        region=RegionNames.Flip,
        statistic=Statistic("flips", "100"),
    ),
    LocationData(
        11002,
        name="Master Acrobat",
        description="Flip 1K times",
        region=RegionNames.Flip,
        statistic=Statistic("flips", "1K"),
        requirements=[
            ItemNames.Loop,
            ItemNames.Megafarm,
            ItemNames.Functions,
        ],
    ),
    LocationData(
        11003,
        name="All the flips",
        description="Flip 10K times",
        region=RegionNames.Flip,
        statistic=Statistic("flips", "10K"),
        requirements=[
            ItemNames.Loop,
            Requirement(ItemNames.Megafarm, 3),
            ItemNames.Functions,
        ],
    ),
    LocationData(
        11004,
        name="Just keep flipping, just keep flipping",
        description="Flip 100K times",
        region=RegionNames.Flip,
        statistic=Statistic("flips", "100K"),
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
        name="Cacti",
        description="Plant a cactus",
        region=RegionNames.Crop,
        achievement="PLANT_CACTUS",
        requirements=[ItemNames.Carrot, ItemNames.Pumpkins, ItemNames.Cactus],
    ),
    LocationData(
        12006,
        name="Trees",
        description="Plant a tree",
        region=RegionNames.Crop,
        achievement="PLANT_TREE",
        requirements=[ItemNames.Trees]
    ),
    # endregion
    # region 13Ks Hay
    LocationData(
        13000,
        name="Hay Fever",
        description="Farm 100 hay",
        region=RegionNames.Hay,
        statistic=Statistic("hay", "100"),
    ),
    LocationData(
        13001,
        name="Hey, Farmer!",
        description="Farm 1K Hay",
        region=RegionNames.Hay,
        statistic=Statistic(key="hay", value="1K"),
        requirements=[
            Requirement(ItemNames.Grass, 2),
            ItemNames.Loop,
        ],
    ),
    LocationData(
        13002,
        name="Cause I have farmed 10K Hay",
        description="Farm 10K hay",
        region=RegionNames.Hay,
        statistic=Statistic("hay", "10K"),
        requirements=[
            ItemNames.Functions,
            ItemNames.Loop,
            ItemNames.Megafarm,
            Requirement(ItemNames.Grass, 3)
        ],
    ),
    LocationData(
        13003,
        name="Hay Master",
        description="Farm 100K hay",
        region=RegionNames.Hay,
        statistic=Statistic("hay", "100K"),
        requirements=[
            ItemNames.Functions,
            ItemNames.Loop,
            Requirement(ItemNames.Megafarm, 2),
            Requirement(ItemNames.Grass, 4),
        ],
    ),
    LocationData(
        13004,
        name="1M Hay",
        description="Farm 1M hay",
        region=RegionNames.Hay,
        statistic=Statistic("hay", "1M"),
        requirements=[
            ItemNames.Functions,
            ItemNames.Loop,
            Requirement(ItemNames.Megafarm, 3),
            Requirement(ItemNames.Grass, 6),
        ],
    ),
    LocationData(
        13005,
        name="10M Hay",
        description="Farm 10M hay",
        region=RegionNames.Hay,
        statistic=Statistic("hay", "10M"),
        requirements=[
            ItemNames.Functions,
            ItemNames.Loop,
            Requirement(ItemNames.Megafarm, 3),
            Requirement(ItemNames.Grass, 7),
        ],
    ),
    LocationData(
        13006,
        name="100M Hay",
        description="Farm 100M hay",
        region=RegionNames.Hay,
        statistic=Statistic("hay", "100M"),
        requirements=[
            ItemNames.Functions,
            ItemNames.Loop,
            Requirement(ItemNames.Megafarm, 4),
            Requirement(ItemNames.Grass, 8),
        ],
    ),
    LocationData(
        13007,
        name="Big Hay Farmer",
        description="Farm 1B hay",
        region=RegionNames.Hay,
        statistic=Statistic("hay", "1B"),
        requirements=[
            ItemNames.Functions,
            ItemNames.Loop,
            Requirement(ItemNames.Megafarm, 5),
            Requirement(ItemNames.Grass, 10),
        ],
    ),
    # endregion
    # region 15Ks Carrot
    LocationData(
        15000,
        name="Must be a bunny",
        description="Farm 100 carrots",
        region=RegionNames.Carrot,
        statistic=Statistic("carrot", "100"),
    ),
    LocationData(
        15001,
        name="Carrot Farmer",
        description="Farm 1K carrots",
        region=RegionNames.Carrot,
        statistic=Statistic("carrot", "1K"),
        requirements=[
            ItemNames.Expand
        ],
    ),
    LocationData(
        15002,
        name="10K carrots",
        description="Farm 10K carrots",
        region=RegionNames.Carrot,
        statistic=Statistic("carrot", "10K"),
        requirements=[
            Requirement(ItemNames.Carrot, 2),
            Requirement(ItemNames.Expand, 2),
        ],
    ),
    LocationData(
        15003,
        name="100K Carrots",
        description="Farm 100K carrots",
        region=RegionNames.Carrot,
        statistic=Statistic("carrot", "100K"),
        requirements=[
            Requirement(ItemNames.Carrot, 4),
            Requirement(ItemNames.Expand, 3),
            ItemNames.Megafarm,
        ],
    ),
    LocationData(
        15004,
        name="All the carrots",
        description="Farm 1M carrots",
        region=RegionNames.Carrot,
        statistic=Statistic("carrot", "1M"),
        requirements=[
            Requirement(ItemNames.Carrot, 6),
            Requirement(ItemNames.Expand, 4),
            Requirement(ItemNames.Megafarm, 2),
        ],
    ),
    LocationData(
        15005,
        name="10M Carrots",
        description="Farm 10M carrots",
        region=RegionNames.Carrot,
        statistic=Statistic("carrot", "10M"),
        requirements=[
            Requirement(ItemNames.Carrot, 7),
            Requirement(ItemNames.Expand, 4),
            Requirement(ItemNames.Megafarm, 3),
        ],
    ),
    LocationData(
        15006,
        name="100M Carrots",
        description="Farm 100M carrots",
        region=RegionNames.Carrot,
        statistic=Statistic("carrot", "100M"),
        requirements=[
            Requirement(ItemNames.Carrot, 8),
            Requirement(ItemNames.Expand, 5),
            Requirement(ItemNames.Megafarm, 3),
        ],
    ),
    LocationData(
        15007,
        name="Orange you glad you're done with carrots?",
        description="Farm 1B carrots",
        region=RegionNames.Carrot,
        statistic=Statistic("carrot", "1B"),
        requirements=[
            Requirement(ItemNames.Carrot, 10),
            Requirement(ItemNames.Expand, 9),
            Requirement(ItemNames.Megafarm, 5),
        ],
    ),
    # endregion
    # region 16Ks Wood
    LocationData(
        16000,
        name="100 Wood",
        description="Farm 100 wood",
        region=RegionNames.Wood,
        statistic=Statistic("wood", "100"),
    ),
    LocationData(
        16001,
        name="Deforestation",
        description="Farm 1K Wood",
        region=RegionNames.Wood,
        statistic=Statistic("wood", "1K"),
        requirements=[ItemNames.Expand],
    ),
    LocationData(
        16002,
        name="10K Wood",
        description="Farm 10K Wood",
        region=RegionNames.Wood,
        statistic=Statistic("wood", "10K"),
        requirements=[
            Requirement(ItemNames.Trees, 2),
            Requirement(ItemNames.Expand, 2),
            Requirement(ItemNames.Megafarm, 1),
        ],
    ),
    LocationData(
        16003,
        name="100K Wood",
        description="Farm 100K Wood",
        region=RegionNames.Wood,
        statistic=Statistic("wood", "100K"),
        requirements=[
            Requirement(ItemNames.Trees, 3),
            Requirement(ItemNames.Expand, 3),
            Requirement(ItemNames.Megafarm, 2),
        ],
    ),
    LocationData(
        16004,
        name="1M Wood",
        description="Farm 1M Wood",
        region=RegionNames.Wood,
        statistic=Statistic("wood", "1M"),
        requirements=[
            Requirement(ItemNames.Trees, 5),
            Requirement(ItemNames.Expand, 5),
            Requirement(ItemNames.Megafarm, 3),
        ],
    ),
    LocationData(
        16005,
        name="100M Wood",
        description="Farm 100M Wood",
        region=RegionNames.Wood,
        statistic=Statistic("wood", "100M"),
        requirements=[
            Requirement(ItemNames.Trees, 8),
            Requirement(ItemNames.Expand, 7),
            Requirement(ItemNames.Megafarm, 4),
        ],
    ),
    LocationData(
        16006,
        name="Big Wood Farmer",
        description="Farm 1B wood",
        region=RegionNames.Wood,
        statistic=Statistic("wood", "1B"),
        requirements=[
            Requirement(ItemNames.Trees, 10),
            Requirement(ItemNames.Expand, 9),
            Requirement(ItemNames.Megafarm, 5),
        ],
    ),
    # endregion
    # region 17Ks Pumpkin
    LocationData(
        17000,
        name="Jack Collector",
        description="Farm 100 pumpkins",
        region=RegionNames.Pumpkins,
        statistic=Statistic("pumpkin", "100"),
    ),
    LocationData(
        17001,
        name="Pumpkin Farmer",
        description="Farm 1K Pumpkins",
        region=RegionNames.Pumpkins,
        statistic=Statistic("pumpkin", "1K"),
        requirements=[
            Requirement(ItemNames.Pumpkins, 2),
            Requirement(ItemNames.Expand, 3),
        ],
    ),
    LocationData(
        17002,
        name="Big Pumpkin Farmer",
        description="Farm 100M pumpkins",
        region=RegionNames.Pumpkins,
        statistic=Statistic("pumpkin", "100M"),
        requirements=[
            Requirement(ItemNames.Pumpkins, 6),
            Requirement(ItemNames.Expand, 4),
        ],
    ),
    # endregion
    # region 18Ks Power
    LocationData(
        18000,
        name="Flower Power",
        description="Farm 100 power",
        region=RegionNames.Sunflower,
        statistic=Statistic("power", "100"),
    ),
    LocationData(
        18001,
        name="Power Farmer",
        description="Farm 1K Power",
        region=RegionNames.Sunflower,
        achievement="POWER_FARMER",
        statistic=Statistic("power", "1K"),
        requirements=[
            Requirement(ItemNames.Expand, 3),
        ],
    ),
    LocationData(
        18002,
        name="Over 9000!",
        description="Farm 9001 power",
        region=RegionNames.Sunflower,
        statistic=Statistic("power", "9001"),
        requirements=[
            Requirement(ItemNames.Expand, 3),
        ],
    ),
    LocationData(
        18003,
        name="Unlimited Power Farmer",
        description="Farm 100K Power",
        region=RegionNames.Sunflower,
        statistic=Statistic("power", "100K"),
        requirements=[
            Requirement(ItemNames.Expand, 3),
        ],
    ),
    # endregion
    # region 19Ks Cacti
    LocationData(
        19000,
        name="A Little Pokey",
        description="Farm 100 cacti",
        region=RegionNames.Cactus,
        statistic=Statistic("cactus", "100"),
        requirements=[ItemNames.Plant]
    ),
    LocationData(
        19001,
        name="Can't touch this (ow!)",
        description="Farm 1K Cacti",
        region=RegionNames.Cactus,
        statistic=Statistic("cactus", "1K")
    ),
    LocationData(
        19002,
        name="Kinda Prickly",
        description="Farm 100K cacti",
        region=RegionNames.Cactus,
        statistic=Statistic("cactus", "100K"),
        requirements=[ItemNames.Plant]
    ),
    LocationData(
        19003,
        name="Big Cactus Farmer",
        description="Farm 1M cacti",
        region=RegionNames.EndGame,
        statistic=Statistic("cactus", "1M"),
        requirements=[ItemNames.Cactus]
    ),
    # endregion
    # region 20Ks Gold
    LocationData(
        20000,
        name="Gold Farmer",
        description="Farm 1K Gold",
        region=RegionNames.Maze,
        statistic=Statistic("gold", "1K")
    ),
    LocationData(
        20001,
        name="Big Gold Farmer",
        description="Farm 100M gold",
        region=RegionNames.EndGame,
        statistic=Statistic("gold", "100M")),
    # endregion
    # region 21Ks Bones
    LocationData(
        21000,
        name="Bone Farmer",
        description="Farm 1K Bones",
        region=RegionNames.Dinos,
        statistic=Statistic("bone", "1K")
    ),
    LocationData(
        21001,
        name="10K Bones",
        description="Farm 10K Bones",
        region=RegionNames.Dinos,
        statistic=Statistic("bone", "10K"),
        requirements=[Requirement(ItemNames.Dinosaurs, 2)],
    ),
    LocationData(
        21002,
        name="1M Bones",
        description="Farm 1M Bones",
        region=RegionNames.Dinos,
        statistic=Statistic("bone", "1M"),
        requirements=[Requirement(ItemNames.Dinosaurs, 3)],
    ),
    LocationData(
        21003,
        name="Big Bone Farmer",
        description="Farm 100M Bones",
        region=RegionNames.Dinos,
        statistic=Statistic("bone", "100M"),
        requirements=[Requirement(ItemNames.Dinosaurs, 5)],
    ),
    # endregion
    # region 22Ks Weird Substance
    LocationData(
        22000,
        name="A bit weird",
        description="Farm 1 weird substance",
        region=RegionNames.WeirdSubstance,
        statistic=Statistic("weird_substance", "1"),
    ),
    LocationData(
        22001,
        name="That's kinda weird",
        description="Farm 100 weird substance",
        region=RegionNames.WeirdSubstance,
        statistic=Statistic("weird_substance", "100"),
    ),
    LocationData(
        22002,
        name="That's really weird",
        description="Farm 1K weird substance",
        region=RegionNames.WeirdSubstance,
        statistic=Statistic("weird_substance", "1K"),
        requirements=[ItemNames.Megafarm],
    ),
    LocationData(
        22003,
        name="10K Weird Substance",
        description="Farm 10K weird substance",
        region=RegionNames.WeirdSubstance,
        statistic=Statistic("weird_substance", "10K"),
        requirements=[
            Requirement(ItemNames.Megafarm, 2),
            Requirement(ItemNames.Expand, 2),
            Requirement(ItemNames.Fertilizer, 2),
        ],
    ),
    LocationData(
        22004,
        name="100K Weird Substance",
        description="Farm 100K weird substance",
        region=RegionNames.WeirdSubstance,
        statistic=Statistic("weird_substance", "100K"),
        requirements=[
            Requirement(ItemNames.Megafarm, 3),
            Requirement(ItemNames.Expand, 3),
            Requirement(ItemNames.Fertilizer, 3),
        ],
    ),
    # endregion
    # region 99Ks Timing
    LocationData(
        99000,
        name="Sunflower Master",
        description="Farm 12K power in 1 minute",
        region=RegionNames.EndGame,
        timed=TimedStatistic("power", "12K", "1m"),
        requirements=[ItemNames.Sunflowers]
    ),
    LocationData(
        99001,
        name="Cactus Master",
        description="Farm 20M cacti in 1 minute",
        region=RegionNames.EndGame,
        timed=TimedStatistic("cacti", "20M", "1m"),
        requirements=[ItemNames.Cactus]
    ),
    LocationData(
        99002,
        name="Dino Master",
        description="Farm 100M bones",
        region=RegionNames.EndGame,
        timed=TimedStatistic("bone", "1M", "1m"),
        requirements=[ItemNames.Dinosaurs]
    ),
    LocationData(
        99003,
        name="Maze Master",
        description="Farm 2M gold in 1 minute",
        region=RegionNames.EndGame,
        timed=TimedStatistic("gold", "2M", "1m"),
        requirements=[ItemNames.Mazes]
    ),
    LocationData(
        99004,
        name="Pumpkin Master",
        description="Farm 20M pumpkins in 1 minute",
        region=RegionNames.EndGame,
        timed=TimedStatistic("pumpkin", "20M", "1m"),
        requirements=[ItemNames.Pumpkins]
    ),
    LocationData(
        99005,
        name="Wood Master",
        description="Farm 1B wood in 1 minute",
        region=RegionNames.EndGame,
        timed=TimedStatistic("wood", "1B", "1m"),
        requirements=[ItemNames.Trees]
    ),
    # endregion
]
"""All location data including names, descriptions, regions, and rules."""
