from collections.abc import Mapping
from typing import Any

import Utils
# Imports of base Archipelago modules must be absolute.
from worlds.AutoWorld import World

from . import items, locations, options, regions, rules, web_world
from .Data.Crops import ALL_CROPS, Crops
from .Data.Region import RegionNames

class TFWRWorld(World):
    """
    Program and optimize a drone to automate a farm and watch it do the work for you. Collect resources to unlock better technology and become the most efficient farmer in the world. Improve your problem solving and coding skills.
    """

    game = "The Farmer Was Replaced"

    web = web_world.TFWRWebWorld()

    options_dataclass = options.TFWROptions
    # Something about mutability causes an error in PyLance
    options: options.TFWROptions # type: ignore

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = RegionNames.Start

    crop_costs: list[Crops]

    def __init__(self, options: Any, player: int):
        super().__init__(options, player)
        self.crop_costs = self.randomize_crop_cost()

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.TFWRItem:
        return items.create_item_with_correct_classification(self, name)
    
    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)
    
    def fill_slot_data(self) -> Mapping[str, Any]:
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        slot_data = self.options.as_dict(
            "goal",
            "crop_cost"
        )
        if options.CropCost:
            for crop in self.crop_costs:
                slot_data["crops." + crop.name] = crop.cost

        return slot_data

    def pre_fill(self):
        from BaseClasses import CollectionState
        from Fill import sweep_from_pool
        state = sweep_from_pool(CollectionState(self.multiworld), self.multiworld.itempool)
        unreachable_locations = [location for location in self.get_locations() if not location.can_reach(state)]
        assert not unreachable_locations, f"All state can't reach all locations: {unreachable_locations}"

    def randomize_crop_cost(self):

        crops = ALL_CROPS
        # The result of any starting crop can be used in a cost
        allowed_costs = {p.result for p in crops if p.starting_crop}

        # Shuffle the order of crops
        self.random.shuffle(crops)

        # For each crop
        for crop in crops:

            # Don't add costs to the starting crops
            if crop.starting_crop:
                pass
            else:
                # Everything else will cost at least 1 item
                min_cost = 1
                # Random chance for costing 2 items (configurable?)
                if self.random.randint(1, 10) > 7:
                    min_cost = 2

                # Don't get too big of a number of ingredients
                k = min(min_cost, len(allowed_costs))

                # Randomly select the ingredients
                chosen_costs: list[str] = self.random.sample(list(allowed_costs), k=k)

                # Add the crop with the randomized cost to the list
                crop.cost = chosen_costs

            if crop.result is not None:
                # This item can be used as an ingredient now
                allowed_costs.add(crop.result)
        return crops