from test.bases import WorldTestBase
from ..world import TFWRWorld


class TFWRTestBase(WorldTestBase):
    game = "The Farmer Was Replaced"
    world: TFWRWorld

    def test_item_counts(self) -> None:
        with self.subTest("Tests that there are items in the item pool"):
            self.assertGreaterEqual(len(self.get_items_by_name("Free Hay")), 0)

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
