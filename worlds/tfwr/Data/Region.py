from dataclasses import dataclass

from .Resources import Resources
from .Rules import RuleNames, Requirement
from .Item import ItemNames


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
    Grass = "GrassSanity"
    Regions: list[str] = [Start, Crop, Flip, Hay, Wood, Carrot, Sunflower, Cactus, WeirdSubstance, Maze, Pumpkins,
                          Drones, Dinos, Grass]


@dataclass
class RegionData:
    name: str
    parent: str = None
    requirements: list[str | Requirement] | None = None
    resource: str = None
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
        resource=Resources.Hay,
    ),
    RegionData(
        name=RegionNames.Wood,
        parent=RegionNames.Crop,
        requirements=[ItemNames.Plant],
        resource=Resources.Wood,
    ),
    RegionData(
        name=RegionNames.Carrot,
        parent=RegionNames.Crop,
        requirements=[ItemNames.Carrot],
        resource=Resources.Carrot,
    ),
    RegionData(
        name=RegionNames.WeirdSubstance,
        parent=RegionNames.Crop,
        requirements=[
            RuleNames.CropsThatCanProduceWeirdSubstance,
            ItemNames.Fertilizer
        ],
    ),
    RegionData(
        name=RegionNames.Maze,
        parent=RegionNames.Crop,
        requirements=[
            ItemNames.Drone_Speed,
            ItemNames.Loop,
            ItemNames.Fertilizer,
            ItemNames.Mazes
        ],
    ),
    RegionData(
        name=RegionNames.Sunflower,
        parent=RegionNames.Crop,
        requirements=[
            ItemNames.Drone_Speed,
            ItemNames.Loop,
            ItemNames.Variables,
            ItemNames.Sunflowers,
            ItemNames.Operators
        ],
        resource=Resources.Power,
    ),
    RegionData(
        name=RegionNames.Pumpkins,
        parent=RegionNames.Crop,
        requirements=[
            ItemNames.Drone_Speed,
            ItemNames.Loop,
            ItemNames.Pumpkins,
            ItemNames.Variables
        ],
        resource=Resources.Pumpkin,
    ),
    RegionData(
        name=RegionNames.Cactus,
        parent=RegionNames.Crop,
        requirements=[
            ItemNames.Drone_Speed,
            ItemNames.Cactus,
            ItemNames.Operators,
            ItemNames.Variables
        ],
        resource=Resources.Cactus,
    ),
    RegionData(
        name=RegionNames.Drones,
        parent=RegionNames.Crop,
        requirements=[
            ItemNames.Megafarm,
            ItemNames.Functions,
        ],
    ),
    RegionData(
        name=RegionNames.Dinos,
        parent=RegionNames.Crop,
        requirements=[
            ItemNames.Dinosaurs,
            Requirement(ItemNames.Expand, 2),
        ],
        resource=Resources.Bone,
    ),
    RegionData(
        name=RegionNames.Grass,
        parent=RegionNames.Start,
    )
]
