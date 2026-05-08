from dataclasses import dataclass

from Options import OptionGroup, PerGameCommonOptions, Toggle


class EasyMode(Toggle):
    """Enable easy mode for beginners. This actually does nothing so far."""
    display_name = "Easy Mode"


@dataclass
class TFWROptions(PerGameCommonOptions):
    easy_mode: EasyMode


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
