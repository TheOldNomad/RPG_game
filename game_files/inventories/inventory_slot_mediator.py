from game_files.entities.player import Player
from game_files.items.armor import Armor
from game_files.items.items import Item
from game_files.items.weapons import Weapon


class InventoryAndActionSlotsMediator:
    def list_all_items(self, player_character: Player) -> None:
        player_character.inventory.list_all_items()
        player_character.weapon_and_armor_slots.view_equipped_items()
        player_character.see_player_state()

    def hand_over_item_to_active_slot(self, equipable_item: Item, player_character: Player) -> None:
        if not isinstance(equipable_item, (Weapon, Armor)):
            print("You cannot equip it, only weapon and armor work")
            return
        player_character.weapon_and_armor_slots.equip_item(equipable_item)
        print(f"{equipable_item} successfully equipped!")

    def get_item_from_active_slot(self, item_to_remove: Weapon | Armor, player_character: Player) -> None:
        if not (item_to_remove, (Weapon, Armor)):
            print("No such item equipped, try harder")
            return
        removed_item = player_character.weapon_and_armor_slots.discard_item(item_to_remove)
        if removed_item is not None:
            player_character.inventory.add_item(removed_item)
            print(f"{item_to_remove} removed to the inventory")
