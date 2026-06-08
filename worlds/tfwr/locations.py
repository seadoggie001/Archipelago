from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location, Region
from .Data.Location import ALL_LOCATION_DATA, LocationData
from .options import valid_options
from .Data.Region import RegionNames

if TYPE_CHECKING:
    from .world import TFWRWorld

ALL_LOCATIONS: list[LocationData] = (
    ALL_LOCATION_DATA
)

# Remember, locations don't have to be completed. These are "steps" along the way to completing the game, but might be optional
LOCATION_NAME_TO_ID: dict[str, int] = {location.name: location.id for location in ALL_LOCATIONS}


class TFWRLocation(Location):
    game = "The Farmer Was Replaced"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: TFWRWorld) -> None:
    create_achieve_locations(world)
    create_events(world)


def create_achieve_locations(world: TFWRWorld) -> None:
    # For each region
    regionName: str
    for regionName in RegionNames.Regions:
        region: Region = world.get_region(regionName)
        # Get all locations with a matching region
        locations = get_location_names_with_ids(
            [location.name for location in ALL_LOCATIONS if location.region == regionName and valid_options(world.options, location.option)]
        )
        # add the locations to the region
        region.add_locations(locations, TFWRLocation)

def create_events(world: TFWRWorld) -> None:
    # This is used to create a location that acts as an event trigger
    # Possibly useful if the player needs to do something to move between regions that isn't related to a location?
    # Something like an in-game button. I can't think of any use in TFWR though.
    pass
