from _collections_abc import Iterator
from abc import ABC, abstractmethod
from collections.abc import ItemsView

from game_files.items_and_inventories.items import (
    AdvancedHealthPotion,
    Armour,
    Axe,
    HealthPotion,
    Item,
    Sword,
    Weapon,
)


class InventoryTemplate(ABC):
    @abstractmethod
    def add_item(self, items_to_add_list: list) -> str:
        pass

    @abstractmethod
    def discard_item(self, item_id: str) -> None:
        pass

    @abstractmethod
    def choose_item(self, item_id: str) -> Item | None:
        pass

    def list_all_items(self) -> None:
        if not self.player_inventory:
            print("The inventory is currently empty")
            return
        for current_item in self.player_inventory:
            print(current_item)


class Inventory(InventoryTemplate):
    def __init__(self) -> None:
        self.player_inventory: list = [
            Sword("Faggot slayer"),
            Axe("N-word crusher"),
            HealthPotion("Baltica 9"),
            AdvancedHealthPotion("Okhota Krepkaya"),
        ]

    def __iter__(self) -> Iterator[tuple[Item]]:
        return iter(self.player_inventory)

    def get_items(self) -> ItemsView:
        return self.player_inventory

    def add_item(self, item_list: list) -> str:
        self.player_inventory.extend(item_list)

    def discard_item(self, item_id: str) -> None:
        self.player_inventory.pop(item_id)

    def choose_item(self, item_index: int) -> Item | None:
        if 0 <= item_index < len(self.player_inventory):
            return self.player_inventory[item_index]
        raise IndexError("item index not found, try again, genius")


class ActiveSlots(ABC):
    @abstractmethod
    def equip_item(self, chosen_item: Item, player_inventory: Inventory) -> None:
        pass

    @abstractmethod
    def discard_item(self, item_to_remove: Item, player_inventory: Inventory) -> None:
        pass

    @abstractmethod
    def get_item_parameters(self, item_equipped: Item) -> int | None:
        pass

    @abstractmethod
    def view_equipped_items(self) -> ItemsView[str, Item]:
        pass


class WeaponSlots(ActiveSlots):
    def __init__(self) -> None:
        self.weapon_slots: dict[str, Weapon | None] = {"main hand": None, "secondary hand": None}
        self.weapon_slot_capacity = 2

    def equip_item(self, chosen_item: Item, player_inventory: Inventory) -> None:
        if isinstance(chosen_item, Weapon) and chosen_item.hand_to_equip in self.weapon_slots:
            self.weapon_slots[chosen_item.hand_to_equip] = chosen_item
            if self.weapon_slots[chosen_item.hand_to_equip] is not None:
                replaced_item = self.weapon_slots[chosen_item.hand_to_equip]
                player_inventory.add_item(replaced_item)
        else:
            print("Wrong item type, dumbass, try again")
            return

    def discard_item(self, item_to_remove: Item, player_inventory: Inventory) -> None:
        item_to_remove = str(input("please, choose the weapon you would like to remove"))
        if item_to_remove in self.weapon_slots:
            removed_item = self.weapon_slots[item_to_remove]
        if self.weapon_slots[item_to_remove] is not None:
            self.weapon_slots[item_to_remove] = None
            player_inventory.add_item(removed_item)

    def get_item_parameters(self, item_equipped: Item) -> int | None:
        if isinstance(item_equipped, Weapon) and item_equipped in self.weapon_slots:
            return item_equipped.item_parameters
        print("Your hand is empty, chief. You must be really brave for going at monsters barehanded!")
        return None

    def view_equiped_items(self) -> ItemsView[str, Item]:
        return self.weapon_slots.items()


class ArmorSlots(ActiveSlots):
    def __init__(self) -> None:
        self.armor_slots: dict[str, Armour | None] = {
            "head": None,
            "torso": None,
            "arms": None,
            "legs": None,
            "feet": None,
        }
        self.armor_slot_capacity = 5

    def equip_item(self, chosen_item: Item, player_inventory: Inventory) -> None:
        if isinstance(chosen_item, Armour) and chosen_item.slot_to_equip in self.armor_slots:
            self.armor_slots[chosen_item.slot_to_equip] = chosen_item
            if self.armor_slots[chosen_item.slot_to_equip] is not None:
                replaced_item = self.armor_slots[chosen_item.slot_to_equip]
                player_inventory.add_item(replaced_item)
        else:
            print("Wrong item type, dumbass, try again")
            return

    def discard_item(self, player_inventory: Inventory) -> None:
        item_to_remove = str(input("please, choose the armor part you would like to remove"))
        if item_to_remove in self.armor_slots:
            removed_item = self.armor_slots[item_to_remove]
        if self.armor_slots[item_to_remove] is not None:
            self.armor_slots[item_to_remove] = None
            player_inventory.add_item(removed_item)

    def get_item_parameters(self, item_equipped: Item) -> int | None:
        if item_equipped in self.armor_slots:
            return item_equipped.item_parameters
        print("This body part is not armored. You must be really brave for going at monsters like that!")
        return None

    def view_equipped_items(self) -> ItemsView[str, Item]:
        return self.armor_slots.items()


# Константные переменные в питоне записываются полностью большими буквами, как в примере с
# INITIAL_PLAYER_INVENTORY
