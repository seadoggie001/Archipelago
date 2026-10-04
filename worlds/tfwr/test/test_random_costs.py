import os

import Utils
from BaseClasses import Location
from Data.Item import ItemNames
from Data.Crops import Crops
from .bases import TFWRTestBase

class TestRandomizedCropLogic(TFWRTestBase):
    """Tests that the randomized crop logic works correctly"""
    def world_setup(self, seed:int|None = None) -> None:
        super().world_setup(self.seed)

    seed = 49855163501941462640
    # Specify the seed to make crop costs deterministic for testing
    # CropCosts: Bush [] Carrot ['wood'] Tree ['wood'] Hay [] Dinosaur ['hay'] Pumpkin ['bone'] Sunflower ['wood', 'wood'] Cactus ['pumpkin']

    options = {
        "goal": 0,
        "crop_cost": True,
    }

    run_default_tests = False

    def test_costs(self) -> None:
        text = ""
        crop_cost: Crops
        for crop_cost in self.world.crop_costs:
            text += f"{crop_cost.name} {str(crop_cost.cost)} "
        print(text)

        with self.subTest("Tests checks accessible with nothing"):
            hello_world: Location = self.world.get_location("Hello World!")

            self.assertTrue(hello_world.can_reach(self.multiworld.state))

        with self.subTest("Tests that pumpkin requires carrot for tilling and bone for crop cost"):
            self.assertAccessDependency(["Pumpkins"], [[
                ItemNames.Carrot
            ]], only_check_listed=True)
            self.assertAccessDependency(["Pumpkins"], [[
                ItemNames.Dinosaurs
            ]], only_check_listed=True)

        with self.subTest("Tests that Sunflowers requires carrot"):
            self.assertAccessDependency(["Sunflowers"], [[
                ItemNames.Carrot
                ]], only_check_listed=True)

        with self.subTest("Create visualization"):
            """ This builds PUML files, it is not a test """
            state = self.multiworld.get_all_state(False)
            state.update_reachable_regions(self.player)
            folder: str = os.getcwd() + "/worlds/tfwr/test/visualization/"
            regions: list[str] = ["Start"]
            for region in regions:
                Utils.visualize_regions(self.world.get_region(region),
                                        folder + region + "_RandomizedCrops.puml",
                                        regions_to_highlight=state.reachable_regions[self.player],
                                        show_entrance_names=True
                                        )
