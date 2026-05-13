from game_files.inventories.player_inventory import Inventory, WeaponAndArmorSlots
from game_files.items.armor import Armor
from game_files.items.items import Item
from game_files.items.weapons import Weapon


class InventoryAndActionSlotsMediator:
    def list_all_items(self, inventory: Inventory, weapon_and_armor_slots: WeaponAndArmorSlots) -> None:
        inventory.list_all_items()
        weapon_and_armor_slots.view_equipped_items()

    def hand_over_item_to_active_slot(self, equipable_item: Item, weapon_and_armor_slots: WeaponAndArmorSlots) -> None:
        if not isinstance(equipable_item, (Weapon, Armor)):
            print("You cannot equip it, only weapon and armor work")
            return
        self.get_item_from_active_slot()
        weapon_and_armor_slots.equip_item(equipable_item)
        print(f"{equipable_item} successfully equipped!")

    def get_item_from_active_slot(
        self, item_to_remove: Item, player_inventory: Inventory, weapon_and_armor_slots: WeaponAndArmorSlots
    ) -> None:
        if not (item_to_remove, (Weapon, Armor)):
            print("No such item equipped, try harder")
            return
        removed_item = weapon_and_armor_slots.discard_item(item_to_remove)
        player_inventory.add_item(removed_item)
        print(f"{item_to_remove} removed to the inventory")
