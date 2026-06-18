from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, Rule, True_, HasAny, CanReachLocation, CanReachRegion
from .Data.Item import ItemNames
from .Data.Location import ALL_LOCATION_DATA, LocationData
from .Data.Region import ALL_REGION_DATA, RegionData
from .Data.Rules import RuleNames, Requirement
from .options import valid_options, Goal

if TYPE_CHECKING:
    from .world import TFWRWorld


# Rules define the requirements to move between regions (as in, use an entrance)


def set_all_rules(world: TFWRWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: TFWRWorld) -> None:
    for region_data in ALL_REGION_DATA:
        if region_data.requirements is not None:
            entrance = world.get_entrance(region_data.entrance_name)
            world.set_rule(entrance, resolve_region_rules(world, region_data))


def set_all_location_rules(world: TFWRWorld) -> None:
    for location_data in ALL_LOCATION_DATA:
        if location_data.requirements is not None and valid_options(world.options, location_data.option):
            location = world.get_location(location_data.name)
            world.set_rule(location, resolve_location_rules(world, location_data))


def resolve_location_rules(world: TFWRWorld, loc: LocationData) -> Rule[TFWRWorld]:
    if loc.statistic is not None:
        cost = next((p.cost for p in world.crop_costs if p.name == loc.statistic.key), None)
        if cost is not None:
            for item_cost in cost:
                parent_loc = next((p for p in ALL_LOCATION_DATA if
                                   p.statistic is not None and p.statistic.key == item_cost and p.statistic.value == loc.statistic.value),
                                  None)
                if parent_loc is not None:
                    return CanReachLocation(parent_loc.name) & resolve_rules(loc.requirements)
    return resolve_rules(loc.requirements)


def resolve_region_rules(world: TFWRWorld, region: RegionData) -> Rule[TFWRWorld]:
    rule = resolve_rules(region.requirements)
    # If this region is for a crop (ie: it produces a resource)
    if region.resource is not None:
        # Find the related crop cost
        crop = next(v for v in world.crop_costs if v.result == region.resource)

        def region_for_cost(cost: str) -> str:
            return next(v for v in ALL_REGION_DATA if v.resource == cost).name

        for cost_item in crop.cost:
            rule &= CanReachRegion(region_for_cost(cost_item))
    return rule

def resolve_rules(loc_requirements: list[Requirement | str]) -> Rule[TFWRWorld]:
    rule: Rule[TFWRWorld] = True_()

    for requirement in loc_requirements:
        # If it's not a rule
        if requirement not in RuleNames.Rules:
            # If it's a string
            if isinstance(requirement, str):
                if requirement in ItemNames.ALL_UPGRADES:
                    rule &= Has(requirement)
                else:
                    # throw some error
                    raise ValueError(
                        "This item is not contained in RULE.Rules or ItemNames.ALL_UPGRADES. Value " + requirement)
            # Handle requirement objects
            elif isinstance(requirement, Requirement):
                rule &= Has(requirement.name, count=requirement.count)
            else:
                raise ValueError("I have no idea what this rule is. " + requirement)
        else:
            match requirement:
                case RuleNames.AnyHatItems:
                    rule &= HasAny(ItemNames.Hats, ItemNames.TopHat)
                case RuleNames.ReallyBigFarm:
                    rule &= Has(ItemNames.Expand, 9)
                case RuleNames.CropsThatCanProduceWeirdSubstance:

                    def find_location_by_id(number):
                        for loc in ALL_LOCATION_DATA:
                            if loc.id == number:
                                return loc.name
                        raise ValueError("Unexpected Location ID not found in data: " + number)

                    rule &= (
                            Has(ItemNames.Grass, 2)
                            # Plant Carrots
                            | (CanReachLocation(find_location_by_id(12002)) & Has(ItemNames.Carrot, 2))
                            # Plant Trees
                            | CanReachLocation(find_location_by_id(12006))
                            # Plant Carrots
                            | (CanReachLocation(find_location_by_id(12005)) & Has(ItemNames.Cactus, 2))
                            # Plant Pumpkins
                            | CanReachLocation(find_location_by_id(12003))
                    )
                case RuleNames.MaxedOutFarm:
                    rule &= Has(ItemNames.Expand, 9)
                    rule &= Has(ItemNames.Drone_Speed, 5)
                    rule &= Has(ItemNames.Megafarm, 5)
                    rule &= Has(ItemNames.Functions)
                case _:
                    # throw some error
                    raise ValueError(
                        "Great job! You made a string for a rule, but forgot to actually make the rule in rules.py[resolve_rules]")
    return rule


def set_completion_condition(world: TFWRWorld) -> None:
    """How do you win?"""
    world.set_completion_rule(
        CanReachLocation("Gold Farmer", options=[OptionFilter(Goal, Goal.option_gold)])
        | CanReachLocation("Size Matters", options=[OptionFilter(Goal, Goal.option_dinosaur_tail)])
    )
