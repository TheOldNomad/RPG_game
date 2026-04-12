from game_files.items_and_inventories.player_inventory import Inventory


class InventoryAndActionSlotsMediator:
    def list_all_items_in_inventory(self, inventory: Inventory) -> None:
        inventory.list_all_items()
    def 