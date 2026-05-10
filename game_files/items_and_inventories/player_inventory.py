from _collections_abc import Iterator
from abc import ABC, abstractmethod
from collections.abc import ItemsView

from game_files.items_and_inventories.items import (
    AdvancedHealthPotion,
    Armour,
    Axe,
    Boots,
    Breastplate,
    Club,
    Dagger,
    Gauntlets,
    HealthPotion,
    Helmet,
    Item,
    Sword,
    Trousers,
    Weapon,
)


class InventoryTemplate(ABC):
    @abstractmethod
    def add_item(self, item_to_add: Item) -> None:
        pass

    @abstractmethod
    def add_multiple_items(self, items_to_add_list: list) -> None:
        pass

    @abstractmethod
    def discard_item(self, item_index: int) -> None:
        pass

    @abstractmethod
    def choose_item(self, item_index: int) -> Item | None:
        pass

    @abstractmethod
    def list_all_items(self) -> None:
        pass


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


class WeaponSlots:
    def __init__(self) -> None:
        self.main_hand: Weapon | None = None
        self.secondary_hand: Weapon | None = None

    def equip_item(self, chosen_item: Weapon) -> None:
        match chosen_item:
            case Sword():
                self.main_hand = chosen_item
            case Axe():
                self.main_hand = chosen_item
            case Dagger():
                self.secondary_hand = chosen_item
            case Club():
                self.secondary_hand = chosen_item
            case _:
                print("Wrong item type, dumbass, try again")

    def discard_item(self, item_to_remove: Weapon) -> None:
        match item_to_remove:
            case Sword():
                item_to_remove = self.main_hand
            case Axe():
                item_to_remove = self.main_hand
            case Dagger():
                item_to_remove = self.secondary_hand
            case Club():
                item_to_remove = self.secondary_hand
            case None:
                print("No item is equipped, cannot discard it")

    def get_item_parameters(self, item_equipped: Weapon) -> int | None:
        if item_equipped in self.weapon_slots:
            return item_equipped.item_parameters
        print("Your hand is empty, chief. You must be really brave for going at monsters barehanded!")
        return None

    def view_equipped_items(self) -> ItemsView[str, Weapon | None]:
        return self.weapon_slots.items()


class ArmorSlots:
    def __init__(self) -> None:
        self.head: Helmet | None = None
        self.torso: Breastplate | None = None
        self.arms: Gauntlets | None = None
        self.legs: Trousers | None = None
        self.feet: Boots | None = None

    def equip_item(self, chosen_item: Armour) -> None:
        match chosen_item:
            case Helmet():
                self.head = chosen_item
            case Breastplate():
                self.torso = chosen_item
            case Gauntlets():
                self.arms = chosen_item
            case Trousers():
                self.legs = chosen_item
            case Boots():
                self.feet = chosen_item
            case _:
                print("Wrong item type, dumbass, try again")

    def discard_item(self, item_to_remove: Armour) -> Armour | None:
        match item_to_remove:
            case Helmet():
                item_to_remove = self.head
            case Breastplate():
                item_to_remove = self.torso
            case Gauntlets():
                item_to_remove = self.arms
            case Trousers():
                item_to_remove = self.legs
            case Boots():
                item_to_remove = self.feet
            case None:
                print("No item is equipped, cannot discard it")
        return item_to_remove

    def get_item_parameters(self, item_equipped: Armour) -> int | None:
        if item_equipped in self.armor_slots:
            return item_equipped.item_parameters
        print("This body part is not armored. You must be really brave for going at monsters like that!")
        return None

    def view_equipped_items(self) -> ItemsView[str, Item | None]:
        return self.armor_slots.items()


# Константные переменные в питоне записываются полностью большими буквами, как в примере с
# INITIAL_PLAYER_INVENTORY
