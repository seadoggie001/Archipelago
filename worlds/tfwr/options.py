from dataclasses import dataclass

from Options import OptionGroup, PerGameCommonOptions, Toggle, Choice, Range
from .Data.Location import Options


class Goal(Choice):
    """Select how the game will end

    - **Gold:** collect 1K gold.
    - **Dinosaur Tail:** create a dinosaur tail 1K blocks long. This is almost the entire farm."""
    display_name = "Goal"

    option_gold = 0
    """Collect 1K gold"""

    option_dinosaur_tail = 1
    """Create a dinosaur with a length of 1K"""


class EarlyRiser(Toggle):
    """Require the ``plant`` item to be located early. Makes starting faster"""
    display_name = "Early Riser"


class GrassSanity(Toggle):
    """Adds a check to each square of the farm. Harvest grass to complete the check."""
    display_name = "Grass Sanity"
    default = False


class CropCost(Toggle):
    """Randomizes the cost of planting crops.

    - Hay and Bushes are always free.
    - Max of 2 items per crop."""
    display_name = "Randomized Crop Cost"
    default = False


class TrapPercentage(Range):
    """Percentage of traps that replace filler items"""
    display_name = "Trap Percentage"
    range_start = 0
    range_end = 100
    default = 1


class CropTarget10(Range):
    """The number of crops to obtain for checks"""
    display_name = "Crop Target - 10"
    range_start = 2 # Because I said so
    range_end = 10 * 1000 # 10K
    default = 10


class CropTarget100(Range):
    """The number of crops to obtain for checks"""
    display_name = "Crop Target - 100"
    range_start = 2 # Because I said so
    range_end = 100 * 1000 # 100K
    default = 100


class CropTarget1K(Range):
    """The number of crops to obtain for checks"""
    display_name = "Crop Target - 1K"
    range_start = 2 # Because I said so
    range_end = 1000 * 1000 # 1M
    default = 1000 # 1K


class CropTarget10K(Range):
    """The number of crops to obtain for checks"""
    display_name = "Crop Target - 10K"
    range_start = 10
    range_end = 10 * 1000 * 1000  # 10M
    default = 10 * 1000  # 10K


class CropTarget100K(Range):
    """The number of crops to obtain for checks"""
    display_name = "Crop Target - 100K"
    range_start = 100
    range_end = 100 * 1000 * 1000  # 100M
    default = 100 * 1000  # 100K


class CropTarget1M(Range):
    """The number of crops to obtain for checks"""
    display_name = "Crop Target - 1M"
    range_start = 1000  # 1K
    range_end = 1000 * 1000 * 1000  # 1B
    default = 1000 * 1000  # 1M


class CropTarget10M(Range):
    """The number of crops to obtain for checks"""
    display_name = "Crop Target - 10M"
    range_start = 10 * 1000 # 10K
    range_end = 10 * 1000 * 1000 * 1000 # 10B
    default = 10 * 1000 * 1000 # 10M


class CropTarget100M(Range):
    """The number of crops to obtain for checks"""
    display_name = "Crop Target - 100M"
    range_start = 100 * 1000 # 100K
    range_end = 100 * 1000 * 1000 * 1000 # 100B
    default = 100 * 1000 * 1000 # 100M


class CropTarget1B(Range):
    """The number of crops to obtain for checks"""
    display_name = "Crop Target - 1B"
    range_start = 1000 * 1000 # 1M
    range_end = 1000 * 1000 * 1000 * 1000 # 1T
    default = 1000 * 1000 * 1000 # 1B


@dataclass
class TFWROptions(PerGameCommonOptions):
    early_riser: EarlyRiser
    grass_sanity: GrassSanity
    goal: Goal
    crop_cost: CropCost
    trap_percentage: TrapPercentage
    crop_target_10: CropTarget10
    crop_target_100: CropTarget100
    crop_target_1K: CropTarget1K
    crop_target_10K: CropTarget10K
    crop_target_100K: CropTarget100K
    crop_target_1M: CropTarget1M
    crop_target_10M: CropTarget10M
    crop_target_100M: CropTarget100M
    crop_target_1B: CropTarget1B


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
            TrapPercentage,
        ],
    ),
    OptionGroup(
        "Sanity",
        [GrassSanity],
    ),
    OptionGroup(
        "Random Crop Targets",
        [
            CropTarget10,
            CropTarget100,
            CropTarget1K,
            CropTarget10K,
            CropTarget100K,
            CropTarget1M,
            CropTarget10M,
            CropTarget100M,
            CropTarget1B,
        ]
    )
]

option_presets = {

}
