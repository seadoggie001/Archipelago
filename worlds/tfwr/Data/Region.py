from dataclasses import dataclass

from .Rules import RuleNames, Requirement
from ..Data.Item import ItemNames


class RegionNames:
    Start = "Start"
    Crop = "Crop"
    Flip = "Flip"
    Hay = "Hay"
    Wood = "Wood"
    Carrot = "Carrot"
    Sunflower = "Sunflower"
    Cactus = "Cactus"
    WeirdSubstance = "WeirdSubstance"
    Maze = "Maze"
    Pumpkins = "Pumpkins"
    Drones = "Drones"
    Dinos = "Dinos"
    EndGame = "EndGame"
    Grass = "GrassSanity"
    Regions: list[str] = [Start, Crop, Flip, Hay, Wood, Carrot, Sunflower, Cactus, WeirdSubstance, Maze, Pumpkins,
                          Drones, Dinos, EndGame, Grass]


@dataclass
class RegionData:
    name: str
    parent: str = None
    requirements: list[str | Requirement] | None = None
    entrance_name: str = ""

    def __post_init__(self):
        if self.parent is not None:
            self.entrance_name = f"{self.parent} to {self.name}"


# This list must be sorted like a hierarchy: Dependent regions come after their parents
ALL_REGION_DATA: list[RegionData] = [
    RegionData(
        name=RegionNames.Start,
    ),
    RegionData(
        name=RegionNames.Crop,
        parent=RegionNames.Start,
        requirements=[ItemNames.Plant],
    ),
    RegionData(
        name=RegionNames.Flip,
        parent=RegionNames.Start,
    ),
    RegionData(
        name=RegionNames.Hay,
        parent=RegionNames.Start,
    ),
    RegionData(
        name=RegionNames.Wood,
        parent=RegionNames.Crop,
        requirements=[ItemNames.Trees],
    ),
    RegionData(
        name=RegionNames.Carrot,
        parent=RegionNames.Crop,
        requirements=[ItemNames.Carrot],
    ),
    RegionData(
        name=RegionNames.WeirdSubstance,
        parent=RegionNames.Crop,
        requirements=[RuleNames.CropsThatCanProduceWeirdSubstance, ItemNames.Fertilizer],
    ),
    RegionData(
        name=RegionNames.Maze,
        parent=RegionNames.WeirdSubstance,
        requirements=[ItemNames.Drone_Speed, ItemNames.Loop, ItemNames.Fertilizer, ItemNames.Mazes],
    ),
    RegionData(
        name=RegionNames.Sunflower,
        parent=RegionNames.Carrot,
        requirements=[ItemNames.Drone_Speed, ItemNames.Loop, ItemNames.Variables, ItemNames.Sunflowers,
                      ItemNames.Operators],
    ),
    RegionData(
        name=RegionNames.Pumpkins,
        parent=RegionNames.Carrot,
        requirements=[ItemNames.Drone_Speed, ItemNames.Loop, ItemNames.Pumpkins, ItemNames.Carrot, ItemNames.Variables],
    ),
    RegionData(
        name=RegionNames.Cactus,
        parent=RegionNames.Pumpkins,
        requirements=[ItemNames.Cactus, ItemNames.Operators],
    ),
    RegionData(
        name=RegionNames.Drones,
        parent=RegionNames.Start,
        requirements=[ItemNames.Megafarm, ItemNames.Functions],
    ),
    RegionData(
        name=RegionNames.Dinos,
        parent=RegionNames.Cactus,
        requirements=[
            ItemNames.Dinosaurs,
            Requirement(ItemNames.Expand, 2),
        ],
    ),
    RegionData(
        name=RegionNames.EndGame,
        parent=RegionNames.Dinos,
        requirements=[ItemNames.Functions],
    ),
    RegionData(
        name=RegionNames.Grass,
        parent=RegionNames.Start,
    )
]
