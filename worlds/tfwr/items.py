from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification
from .Data.Item import ALL_ITEM_DATA, FILLER_ITEM_DATA, REGULAR_ITEM_DATA, TRAP_ITEM_DATA, ItemNames

if TYPE_CHECKING:
    from .world import TFWRWorld


@dataclass
class ItemData:
    name: str
    id: int
    count: int = 1
    classification: ItemClassification = ItemClassification.progression
    secondary_count: int = 0
    secondary_classification: ItemClassification = ItemClassification.filler


ITEM_NAME_TO_ID: dict[str, int] = {item.name: item.id for item in ALL_ITEM_DATA}

DEFAULT_ITEM_CLASSIFICATIONS: dict[str, ItemClassification] = {item.name: item.classification for item in ALL_ITEM_DATA}


class TFWRItem(Item):
    game = "The Farmer Was Replaced"


def get_random_filler_item_name(world: TFWRWorld) -> str:
    # if the random number is under the percentage
    if world.random.randint(0, 99) < world.options.trap_percentage:
        # it's a trap
        return world.random.choice(TRAP_ITEM_DATA).name
    # return a filler item
    return world.random.choice(FILLER_ITEM_DATA).name


def create_item_with_correct_classification(world: TFWRWorld, name: str,
                                            classification: ItemClassification | None = None) -> TFWRItem:
    if classification is None:
        classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return TFWRItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: TFWRWorld) -> None:

    if world.options.early_riser:
        world.multiworld.local_early_items[world.player][ItemNames.Plant] = 1

    item_pool: list[TFWRItem] = []
    # Create every upgrade item
    for item in REGULAR_ITEM_DATA:
        # for each copy needed
        for i in range(0, item.count):
            item_pool.append(create_item_with_correct_classification(world, item.name, item.classification))
        # for each secondary copy
        for i in range(0, item.secondary_count):
            item_pool.append(
                create_item_with_correct_classification(world, item.name, item.secondary_classification))

    # Get count of items
    number_of_items: int = len(item_pool)
    # Get count of missing items
    number_of_unfilled_locations: int = len(world.multiworld.get_unfilled_locations(world.player))
    # How many filler items should we create?
    needed_number_of_filler_items: int = number_of_unfilled_locations - number_of_items
    # Create filler items
    item_pool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    # Save the items to the multiworld
    world.multiworld.itempool += item_pool
