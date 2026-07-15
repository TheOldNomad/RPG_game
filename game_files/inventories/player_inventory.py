from collections.abc import Iterator

from game_files.items.items import Item
from game_files.items.potions import AdvancedHealthPotion, HealthPotion
from game_files.items.weapons import Axe, Sword


class Inventory:
    def __init__(self) -> None:
        self.player_inventory: list = [
            Sword("Faggot slayer"),
            Axe("N-word crusher"),
            HealthPotion("Baltica 9"),
            AdvancedHealthPotion("Okhota Krepkaya"),
        ]

    def __iter__(self) -> Iterator[tuple[Item]]:
        return iter(self.player_inventory)

    def get_items(self) -> list:
        return self.player_inventory

    def add_item(self, item_to_add: Item) -> None:
        self.player_inventory.append(item_to_add)

    def add_multiple_items(self, items_to_add_list: list) -> None:
        self.player_inventory.extend(items_to_add_list)

    def discard_item(self, item_index: int) -> None:
        self.player_inventory.pop(item_index)

    def choose_item(self, item_index: int) -> Item | None:
        if 0 <= item_index < len(self.player_inventory):
            return self.player_inventory[item_index]
        raise IndexError("item index not found, try again, genius")

    def list_all_items(self) -> None:
        if not self.player_inventory:
            print("The inventory is currently empty")
            return
        for current_item in self.player_inventory:
            print(current_item)

    def get_health_potion_parameters(self, potion_to_use: HealthPotion) -> int:
        return potion_to_use.item_parameters
