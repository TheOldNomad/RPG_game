from game_files.items_and_inventories.items import Armour, Item, Weapon
from game_files.items_and_inventories.player_inventory import ActiveSlots, Inventory


class ItemEquipper:
    def hand_over_item_to_active_slot(
        self, equipable_item: Item, player_inventory: Inventory, weapon_slots: ActiveSlots, armor_slots: ActiveSlots
    ) -> None:
        if not isinstance(equipable_item, (Weapon, Armour)):
            print("You cannot equip it, only weapon and armor work")
            return
        if isinstance(equipable_item, Weapon):
            weapon_slots.equip_item(equipable_item, player_inventory)
        else:
            armor_slots.equip_item(equipable_item, player_inventory)
