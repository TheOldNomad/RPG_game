from _collections_abc import Iterator
from abc import ABC, abstractmethod
from collections.abc import ItemsView

from game_files.items.items import (
    AdvancedHealthPotion,
    Armour,
    Axe,
    HealthPotion,
    Item,
    Potion,
    Sword,
    Weapon,
)


class InventoryTemplate(ABC):
    @abstractmethod
    def add_item(self, picked_up_item: Item) -> str:
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

    def choose_item(self, item_id: str) -> Item | None:
        return self.player_inventory[item_id]


# def get_weapon_slot_key():
#     self.player_inventory.keys


class ActiveInventory(InventoryTemplate):
    def __init__(self) -> None:
        self.armor_slots: dict[str, Armour | None] = {
            "head": None,
            "torso": None,
            "arms": None,
            "legs": None,
            "feet": None,
        }
        self.armor_slot_capacity = 5

        self.weapon_slots: dict[str, Weapon | None] = {"main hand": None, "secondary hand": None}
        self.weapon_slot_capacity = 2

    def add_item(self, item_id: str) -> None:
        chosen_item = self.player_inventory.choose_item(item_id)
        if isinstance(chosen_item, Weapon) and chosen_item.hand_to_equip in self.weapon_slots:
            self.weapon_slots[chosen_item.hand_to_equip] = chosen_item
            if self.armor_slots[chosen_item.hand_to_equip] is not None:
                replaced_item = self.weapon_slots[chosen_item.hand_to_equip]
                self.player_inventory.add_item(replaced_item)
        else:
            print("Wrong item type, dumbass, try again")
            return

    def equip_armor(self, item_id: str) -> None:
        chosen_item = self.player_inventory.choose_item(item_id)
        if isinstance(chosen_item, Armour) and chosen_item.slot_to_equip in self.armor_slots:
            self.armor_slots[chosen_item.slot_to_equip] = chosen_item
            if self.armor_slots[chosen_item.slot_to_equip] is not None:
                replaced_item = self.armor_slots[chosen_item.slot_to_equip]
                self.player_inventory.add_item(replaced_item)
        else:
            print("Wrong item type, dumbass, try again")
            return

    def discard_item(self) -> None:
        item_to_discard = str(input("please, choose the armor part you would like to remove"))
        if item_to_discard in self.armor_slots:
            removed_item = self.armor_slots[item_to_discard]
        if self.armor_slots[item_to_discard] is not None:
            self.armor_slots[item_to_discard] = None
            self.player_inventory.add_item(removed_item)

    def choose_item(self, item_id):  # - плейсхолдер, исправить на нормальный метод
        return super().choose_item(item_id)

    def view_items(self) -> ItemsView[str, Item]:
        return self.active_slots.items()


# class ActiveInventory(InventoryTemplate):
#     def __init__(self) -> None:
#         self.armour_slots = {"head": None, "torso": None, "arms": None, "legs": None, "feet": None}
#         self.weapon_slots = {"hand 1": None, "hand 2": None}
#         self.armour_slot_capacity = 5
#         self.weapon_slot_capacity = 2
#         self.supported_item_type = Armour
#         self.accepted_item_type = Weapon

#     def add_item(self, item_id: str, chosen_item: Item) -> None:
#         if len(self.active_slots) >= self.slot_capacity:
#             print("You cannot add items past the set limit. Haven't you played other RPGs, stupid?")
#             return
#         if not isinstance(chosen_item, (Armour, Weapon)):
#             print("Wrong item type, dumbass, try again")
#             return
#         chosen_item = self.player_inventory.choose_item(item_id)
#         self.active_slots[item_id] = chosen_item

#     def discard_item(self, item_id: str) -> None:
#         removed_item = self.active_slots.pop(item_id)
#         self.player_inventory.pickup_item(removed_item)

#     def view_items(self) -> ItemsView[str, Item]:
#         return self.active_slots.items()


# Дописать цикл так, чтобы меню стало «интерактивным» — можно открывать инвентарь,
# экипировать предметы и возвращаться без выхода из функции
# Написать повторный цикл, чтобы пользователь мог экипировать несколько предметов за раз
# Как вариант - воспользоваться enum
# Константные переменные в питоне записываются полностью большими буквами, как в примере с
# INITIAL_PLAYER_INVENTORY
