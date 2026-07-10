from dataclasses import dataclass

from Options import OptionGroup, PerGameCommonOptions, Toggle, Choice
from .Data.Location import Options


class Goal(Choice):
    """Select how the game will end"""
    display_name = "Goal"

    option_gold = 0
    """Collect 1K gold"""

    option_dinosaur_tail = 1
    """Create a dinosaur with a length of 1K"""


class EarlyRiser(Toggle):
    """Require `plant` to be located early. Makes starting faster"""
    display_name = "Early Riser"


class GrassSanity(Toggle):
    """Adds a check to each square of the farm. Harvest grass there to complete the check."""
    display_name = "Grass Sanity"
    default = False


class CropCost(Toggle):
    display_name = "Randomized Crop Cost"
    default = False


@dataclass
class TFWROptions(PerGameCommonOptions):
    early_riser: EarlyRiser
    grass_sanity: GrassSanity
    goal: Goal
    crop_cost: CropCost


def valid_options(options: TFWROptions, option: str | None) -> bool:
    """Checks if a Location should be included in the world"""
    if option == Options.GrassSanity:
        return options.grass_sanity.value == 1
    elif option == "":
        return True
    elif option is None:
        return True
    return True


option_groups = [
    OptionGroup(
        "General",
        [
            Goal,
            EarlyRiser,
            CropCost,
        ],
    ),
    OptionGroup(
        "Sanity",
        [GrassSanity],
    )
]

option_presets = {

}
