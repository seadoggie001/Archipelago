from dataclasses import dataclass

from Options import OptionGroup, PerGameCommonOptions, Toggle
from .Data.Location import Options

class EasyMode(Toggle):
    """Enable easy mode for beginners. This actually does nothing so far."""
    display_name = "Easy Mode"


class EarlyRiser(Toggle):
    """Require plant to be located early. Makes starting faster"""
    display_name = "Early Riser"


class GrassSanity(Toggle):
    """Plant grass on each square of the farm"""
    display_name = "Grass Sanity"
    default = False


@dataclass
class TFWROptions(PerGameCommonOptions):
    easy_mode: EasyMode
    early_riser: EarlyRiser
    grass_sanity: GrassSanity


def valid_options(options: TFWROptions, option: str | None) -> bool:
    """Checks if the options on a Location are currently valid for this world"""
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
        [EasyMode],
    )
]

option_presets = {
    "Easy Mode": {
        "easy_mode": True,
    },
    "Hard Mode": {
        "easy_mode": False,
    },
}
