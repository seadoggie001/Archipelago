from __future__ import annotations

from typing import TYPE_CHECKING, Counter

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule, True_, HasAny, CanReachLocation
from .Data.Item import ItemNames
from .Data.Location import ALL_LOCATION_DATA, Requirement
from .Data.Region import RegionNames, ALL_REGION_DATA
from .options import EasyMode
from .Data.Rules import RuleNames

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
            world.set_rule(entrance, HasAll(*region_data.requirements))
        elif region_data.name == RegionNames.EndGame:
            entrance = world.get_entrance(region_data.entrance_name)
            world.set_rule(entrance, Has(ItemNames.Expand, 9))


def set_all_location_rules(world: TFWRWorld) -> None:
    for location_data in ALL_LOCATION_DATA:
        if location_data.requirements is not None:
            location = world.get_location(location_data.name)
            world.set_rule(location, resolve_rules(location_data.requirements))


def resolve_rules(loc_requirements: list[Requirement | str]) -> Rule[TFWRWorld]:
    rule = True_()

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
                    rule &= (
                            HasAll(ItemNames.Grass, ItemNames.Grass + "++")
                            | (HasAll(ItemNames.Carrot, ItemNames.Carrot + "++"))
                            | Has(ItemNames.Trees)
                            | (HasAll(ItemNames.Cactus, ItemNames.Cactus + "++"))
                            | Has(ItemNames.Pumpkins)
                    )
                case _:
                    # throw some error
                    raise ValueError(
                        "Great job! You made a string for a rule, but forgot to actually make the rule in rules.py[resolve_rules]")
    return rule


def set_completion_condition(world: TFWRWorld) -> None:
    """How do you win?"""
    world.set_completion_rule(
        CanReachLocation("Gold Farmer", options=[OptionFilter(EasyMode, True)])
        | CanReachLocation("Size Matters", options=[OptionFilter(EasyMode, False)])
    )
