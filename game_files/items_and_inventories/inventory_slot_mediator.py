from game_files.items_and_inventories.items import Armour, Item, Weapon
from game_files.items_and_inventories.player_inventory import ArmorSlots, Inventory, WeaponSlots


class InventoryAndActionSlotsMediator:
    def list_all_items(self, inventory: Inventory, weapon_slots: WeaponSlots, armor_slots: ArmorSlots) -> None:
        inventory.list_all_items()
        weapon_slots.view_equipped_items()
        armor_slots.view_equipped_items()

    def hand_over_item_to_active_slot(
        self, equipable_item: Item, player_inventory: Inventory, weapon_slots: WeaponSlots, armor_slots: ArmorSlots
    ) -> None:
        if not isinstance(equipable_item, (Weapon, Armour)):
            print("You cannot equip it, only weapon and armor work")
            return
        if isinstance(equipable_item, Weapon):
            self.get_item_from_active_slot()
            weapon_slots.equip_item(equipable_item, player_inventory)
        else:
            self.get_item_from_active_slot()
            armor_slots.equip_item(equipable_item, player_inventory)
        print(f"{equipable_item} successfully equipped!")

    def get_item_from_active_slot(
        self, item_to_remove: Item, player_inventory: Inventory, weapon_slots: WeaponSlots, armor_slots: ArmorSlots
    ) -> None:
        if not (item_to_remove, (Weapon, Armour)):
            print("No such item equipped, try harder")
            return
        if isinstance(item_to_remove, Weapon):
            removed_item = weapon_slots.discard_item(item_to_remove, player_inventory)
            player_inventory.add_item(removed_item)
        else:
            removed_item = armor_slots.discard_item(item_to_remove, player_inventory)
            player_inventory.add_item(removed_item)
        print(f"{item_to_remove} removed to the inventory")
