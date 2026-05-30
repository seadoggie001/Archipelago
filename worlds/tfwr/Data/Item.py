from dataclasses import dataclass
from BaseClasses import ItemClassification


@dataclass
class ItemData:
    id: int
    name: str
    count: int = 1
    classification: ItemClassification = ItemClassification.progression
    secondary_count: int = 0
    secondary_classification: ItemClassification = ItemClassification.filler


class ItemNames:
    """Upgrades in game. Used as items."""
    Loop = "Loop"
    Drone_Speed = "Drone Speed"
    Hats = "Hats"
    Grass = "Grass"
    Expand = "Expand"
    Plant = "Plant"
    """Plant anything. Also gives bushes."""
    Carrot = "Carrot"
    Watering = "Watering"
    Cactus = "Cactus"
    Fertilizer = "Fertilizer"
    Sunflowers = "Sunflowers"
    Mazes = "Mazes"
    """Unlocks or expands the max maze size"""
    TopHat = "Top Hat"
    Trees = "Trees"
    Pumpkins = "Pumpkins"
    Polyculture = "Polyculture"
    Dinosaurs = "Dinosaurs"
    Megafarm = "Megafarm"
    """Drones"""
    TheFarmersRemains = "TheFarmersRemains"
    Debug = "Debug"
    MoreDebug = "More Debug"
    Timing = "Timing"
    Simulation = "Simulation"
    Operators = "Operators"
    Senses = "Senses"
    Variables = "Variables"
    Functions = "Functions"
    Import = "Import"
    Utilities = "Utilities"
    Lists = "Lists"
    Dictionaries = "Dictionaries"
    Costs = "Costs"
    Unlock = "Unlock"
    Rickroll = "Rickroll"
    ALL_UPGRADES: list[str] = [
        Loop, Drone_Speed, Hats, Grass, Expand, Plant, Carrot, Watering, Cactus, Fertilizer, Sunflowers,
        Mazes, TopHat, Trees, Pumpkins, Polyculture,
        Dinosaurs, Megafarm, TheFarmersRemains,
        Debug, MoreDebug, Timing, Simulation,
        Operators, Senses, Variables, Functions, Import, Utilities,
        Lists, Dictionaries, Costs, Unlock, Rickroll
    ]


UpgradeName = "++"

FILLER_ITEM_DATA: list[ItemData] = [
    ItemData(
        id=12001,
        name="Free Hay",
        classification=ItemClassification.filler
    ),
]

REGULAR_ITEM_DATA: list[ItemData] = [
    ItemData(
        id=11001,
        name=ItemNames.Loop
    ),
    ItemData(
        id=11002,
        name=ItemNames.Drone_Speed,
        count=5
    ),
    ItemData(
        id=11003,
        name=ItemNames.Hats
    ),
    ItemData(
        id=11004,
        name=ItemNames.Grass,
        count=10,
    ),
    ItemData(
        id=11005,
        name=ItemNames.Expand,
        count=9
    ),
    ItemData(
        id=11006,
        name=ItemNames.Plant
    ),
    ItemData(
        id=11007,
        name=ItemNames.Carrot,
        count=10
    ),
    ItemData(
        id=11008,
        name=ItemNames.Watering,
        count=1,
        secondary_classification=ItemClassification.filler,
        secondary_count=8,
    ),
    ItemData(
        id=11009,
        name=ItemNames.Fertilizer,
        count=4
    ),
    ItemData(
        id=11010,
        name=ItemNames.Sunflowers
    ),
    ItemData(
        id=11011,
        name=ItemNames.Mazes,
        secondary_count=5
    ),
    ItemData(
        id=11012,
        name=ItemNames.TopHat,
    ),
    ItemData(
        id=11013,
        name=ItemNames.Trees,
        count=10,
    ),
    ItemData(
        id=11014,
        name=ItemNames.Pumpkins,
        count=10
    ),
    ItemData(
        id=11016,
        name=ItemNames.Polyculture,
        count=5,
        classification=ItemClassification.useful
    ),
    ItemData(
        id=11017,
        name=ItemNames.Cactus,
        secondary_count=5
    ),
    ItemData(
        id=11018,
        name=ItemNames.Dinosaurs,
        count=6,
    ),
    ItemData(
        id=11019,
        name=ItemNames.TheFarmersRemains
    ),
    ItemData(
        id=11020,
        name=ItemNames.Megafarm,
        count=5
    ),
    ItemData(
        id=11021,
        name=ItemNames.Debug
    ),
    ItemData(
        id=11022,
        name=ItemNames.MoreDebug,
        count=1,
        classification=ItemClassification.filler
    ),
    ItemData(
        id=11023,
        name=ItemNames.Timing,
        count=1,
        classification=ItemClassification.filler
    ),
    ItemData(
        id=11024,
        name=ItemNames.Simulation,
        count=1,
        classification=ItemClassification.filler
    ),
    ItemData(
        id=11026,
        name=ItemNames.Operators
    ),
    ItemData(
        id=11027,
        name=ItemNames.Senses,
        count=1,
        classification=ItemClassification.filler
    ),
    ItemData(
        id=11028,
        name=ItemNames.Variables
    ),
    ItemData(
        id=11029,
        name=ItemNames.Functions
    ),
    ItemData(
        id=11030,
        name=ItemNames.Import
    ),
    ItemData(
        id=11031,
        name=ItemNames.Utilities,
        count=1,
        classification=ItemClassification.filler
    ),
    ItemData(
        id=11032,
        name=ItemNames.Lists
    ),
    ItemData(
        id=11033,
        name=ItemNames.Dictionaries
    ),
    ItemData(
        id=11034,
        name=ItemNames.Costs,
        classification=ItemClassification.filler
    ),
    ItemData(
        id=11035,
        name=ItemNames.Unlock,
        classification=ItemClassification.filler
    ),
    ItemData(
        id=11036,
        name=ItemNames.Rickroll,
        classification=ItemClassification.trap
    )
]

ALL_ITEM_DATA: list[ItemData] = (
        REGULAR_ITEM_DATA
        + FILLER_ITEM_DATA
)
