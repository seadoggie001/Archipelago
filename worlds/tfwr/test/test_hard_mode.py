import os

import Utils
from BaseClasses import Location, Region
from .bases import TFWRTestBase
from ..Data.Region import RegionNames


class TestHardModeLogic(TFWRTestBase):
    """I'm really just copying APQuest for now"""

    options = {
        "easy_mode": 0,
        "grass_sanity": 0,
    }

    run_default_tests = False

    def test_hard_mode_access(self) -> None:
        with self.subTest("Tests checks accessible with nothing"):
            hello_world: Location = self.world.get_location("Hello World!")

            self.assertTrue(hello_world.can_reach(self.multiworld.state))

        with self.subTest("Regions are set up correctly"):
            start: Region = self.world.get_region(RegionNames.Start)
            self.assertEqual(len(start.entrances), 0, "Start is the start, it shouldn't have entrances")
            self.assertTrue(start.can_reach(self.multiworld.state), "Start should always be accessible")

            crop: Region = self.world.get_region(RegionNames.Crop)
            self.assertEqual(len(crop.entrances), 1, "Crop should have an entrance from Start")

        with self.subTest("Create visualization"):
            """ This builds PUML files, it is not a test """
            state = self.multiworld.get_all_state(False)
            state.update_reachable_regions(self.player)
            folder: str = os.getcwd() + "/worlds/tfwr/test/visualization/"
            regions: list[str] = ["Start"]
            for region in regions:
                Utils.visualize_regions(self.world.get_region(region),
                                        folder + region + "_Hard.puml",
                                        regions_to_highlight=state.reachable_regions[self.player],
                                        )

        with self.subTest("Tests that Grass sanity is missing"):
            grass_region = self.world.get_region(RegionNames.Grass)
            loc_count = len(grass_region.locations)
            self.assertEqual(loc_count, 0, "Grass sanity locations should be missing")