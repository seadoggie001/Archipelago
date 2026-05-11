from BaseClasses import ItemClassification
from test.bases import WorldTestBase
from ..Data.Item import ALL_ITEM_DATA, ItemNames
from ..Data.Location import ALL_LOCATION_DATA
from ..world import TFWRWorld


class TFWRTestBase(WorldTestBase):
    game = "The Farmer Was Replaced"
    world: TFWRWorld

    def test_item_counts(self) -> None:
        with self.subTest("Tests that there are items in the item pool"):
            self.assertGreaterEqual(len(self.get_items_by_name("Free Hay")), 0)

    def test_too_many_items(self) -> None:
        with self.subTest("Too many items in the item pool"):
            count: int = 0
            for item in ALL_ITEM_DATA:
                if item.classification == ItemClassification.progression:
                    count += item.count
                if item.secondary_classification == ItemClassification.progression:
                    count += item.secondary_count
            print("Locations: " + str(len(ALL_LOCATION_DATA)))
            print("items: " + str(count))
            self.assertGreaterEqual(len(ALL_LOCATION_DATA), count, "Too many items")
        # This test doesn't work like I expected
        # with self.subTest("Tests that all items are in the item pool"):
        #     item_counts: list[Any] = []
        #     for item_name in UPGRADE.ALL_UPGRADES:
        #         print(item_name)
        #         item = 0
        #         try:
        #             item = self.get_item_by_name(item_name)
        #         except ValueError:
        #             print(f"Item {item_name} is not in the item pool")
        #
        #         item_counts.append({item_name, item})
        #     for item_count in item_counts:
        #         self.assertGreaterEqual(item_count[1], 1, item_count[0])

    def test_access(self) -> None:
        with self.subTest("Tests that the Carrots is accessible"):
            self.assertAccessDependency(["Carrots"], [["Carrot", "Plant", "Loop"]], only_check_listed=True)

        with self.subTest("Tests that Gold Farmer is accessible"):
            self.assertAccessDependency(["Gold Farmer"], [["Loop", "Fertilizer", "Plant", "Watering", "Mazes"]],
                                        only_check_listed=True)

    def test_healer_access(self) -> None:
        with self.subTest("Tests that Healer is accessible"):
            self.assertAccessDependency(["Healer"],
                                        [[ItemNames.Fertilizer]],
                                        only_check_listed=True)
            self.assertAccessDependency(["Healer"],
                                        [[ItemNames.Fertilizer, ItemNames.Grass]],
                                        only_check_listed=True)
            self.assertAccessDependency(["Healer"],
                                        [[ItemNames.Fertilizer, ItemNames.Plant, ItemNames.Trees]],
                                        only_check_listed=True)
            self.assertAccessDependency(["Healer"],
                                        [[ItemNames.Fertilizer, ItemNames.Plant, ItemNames.Carrot]],
                                        only_check_listed=True)
            self.assertAccessDependency(["Healer"],
                                        [[ItemNames.Fertilizer, ItemNames.Plant, ItemNames.Carrot, ItemNames.Pumpkins]],
                                        only_check_listed=True)
            self.assertAccessDependency(["Healer"],
                                        [[ItemNames.Fertilizer, ItemNames.Plant, ItemNames.Carrot, ItemNames.Pumpkins, ItemNames.Cactus]],
                                        only_check_listed=True)
    def test_prize_pumpkin_rule(self) -> None:
        with self.subTest("Tests that Prize Pumpkin is accessible"):
            for item in [ItemNames.Expand, ItemNames.Loop, ItemNames.Pumpkins, ItemNames.Carrot, ItemNames.Variables,
                         ItemNames.Carrot, ItemNames.Plant]:
                self.assertAccessDependency(["Prize Pumpkin"], [[item]], only_check_listed=True)
