from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region
from .Data.Region import ALL_REGION_DATA, RegionData

if TYPE_CHECKING:
    from .world import TFWRWorld


def __post_init__(self):
    if self.parent is not None:
        self.entrance_name = f"{self.parent} to {self.name}"


def create_and_connect_regions(world: TFWRWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: TFWRWorld) -> None:
    # Create regions and add them to the world object here.
    regions: list[Region] = [Region(region.name, world.player, world.multiworld) for region in ALL_REGION_DATA]

    # variable = Region("Name", world.player, world.multiworld)

    # Add all regions to a list

    # Some regions might be optional
    # if ####:
    #     regions.append(Region("Optional Region", world.player, world.multiworld))

    # Be sure to use += to avoid overwriting regions
    world.multiworld.regions += regions


def connect_regions(world: TFWRWorld) -> None:
    """Connect regions via entrances"""

    # Do nothing. Defer connecting the regions until rule generation to simplify logic.
