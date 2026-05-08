from dataclasses import dataclass

from ..Data.Item import ItemNames


class RegionNames:
    Start = "Start"
    Loops = "Loops"
    Sunflower = "Sunflower"
    Cactus = "Cactus"
    Maze = "Maze"
    Pumpkins = "Pumpkins"
    Drones = "Drones"
    Dinos = "Dinos"
    EndGame = "EndGame"
    Regions: list[str] = [Start, Loops, Sunflower, Cactus, Maze, Pumpkins, Drones, Dinos, EndGame]


@dataclass
class RegionData:
    name: str
    parent: str = None
    requirements: list[str] | None = None
    entrance_name: str = ""

    def __post_init__(self):
        if self.parent is not None:
            self.entrance_name = f"{self.parent} to {self.name}"


# This list must be sorted like a hierarchy: Dependent regions come after their parents
ALL_REGION_DATA: list[RegionData] = [
    RegionData(
        name=RegionNames.Start
    ),
    RegionData(
        name=RegionNames.Loops,
        parent=RegionNames.Start,
        requirements=[ItemNames.Loop]
    ),
    RegionData(
        name=RegionNames.Maze,
        parent=RegionNames.Loops,
        requirements=[ItemNames.Fertilizer, ItemNames.Mazes, ItemNames.Plant, ItemNames.Watering]
    ),
    # ToDo: Does this really need to have a parent of Maze? It could be Loops, right?
    RegionData(
        name=RegionNames.Sunflower,
        parent=RegionNames.Maze,
        requirements=[ItemNames.Variables, ItemNames.Plant, ItemNames.Sunflowers, ItemNames.Operators]
    ),
    RegionData(
        name=RegionNames.Pumpkins,
        parent=RegionNames.Loops,
        requirements=[ItemNames.Pumpkins, ItemNames.Plant, ItemNames.Carrot, ItemNames.Variables]
    ),
    RegionData(
        name=RegionNames.Cactus,
        parent=RegionNames.Pumpkins,
        requirements=[ItemNames.Cactus, ItemNames.Operators]
    ),
    # ToDo: This could probably connect to Loops instead. It may need a few speed upgrades though.
    RegionData(
        name=RegionNames.Drones,
        parent=RegionNames.Sunflower,
        requirements=[ItemNames.Megafarm, ItemNames.Functions]
    ),
    RegionData(
        name=RegionNames.Dinos,
        parent=RegionNames.Cactus,
        requirements=[ItemNames.Dinosaurs, ItemNames.Plant, ItemNames.Carrot]
    ),
    RegionData(
        name=RegionNames.EndGame,
        parent=RegionNames.Drones,
        requirements=[ItemNames.Functions]
    ),
]
