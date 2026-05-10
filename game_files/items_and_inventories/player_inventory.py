from collections.abc import ItemsView, Iterator

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
    OneHandedMainWeapon,
    OneHandedSecondaryWeapon,
    Sword,
    Trousers,
    Weapon,
)


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


class WeaponSlots:
    def __init__(self) -> None:
        self.main_hand: OneHandedMainWeapon | None = None
        self.secondary_hand: OneHandedSecondaryWeapon | None = None

    def equip_item(self, chosen_item: Weapon) -> None:
        match chosen_item:
            case Sword() | Axe():
                self.main_hand = chosen_item
            case Dagger() | Club():
                self.secondary_hand = chosen_item
            case _:
                print("Wrong item type, dumbass, try again")

    def discard_item(self, item_to_remove: OneHandedMainWeapon | OneHandedSecondaryWeapon | None) -> None:
        match item_to_remove:
            case Sword() | Axe():
                item_to_remove = self.main_hand
                self.main_hand = None
            case Dagger() | Club():
                item_to_remove = self.secondary_hand
                self.secondary_hand = None
            case _:
                print("Wrong item type")
        if item_to_remove is None:
            print("No item is equipped, cannot discard it")
        return item_to_remove

    def get_item_parameters(self, currently_equipped_item: Weapon | None) -> int | None:
        match currently_equipped_item:
            case Sword() | Axe():
                currently_equipped_item = self.main_hand
            case Dagger() | Club():
                currently_equipped_item = self.secondary_hand
            case _:
                print("Wrong item type")
        if currently_equipped_item is None:
            print("No weapon here. You must be really brave for going at monsters like that!")
            return None
        return currently_equipped_item.item_parameters

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
                return

    def discard_item(self, item_to_remove: Armour | None) -> None:
        match item_to_remove:
            case Helmet():
                item_to_remove = self.head
                self.head = None
            case Breastplate():
                item_to_remove = self.torso
                self.torso = None
            case Gauntlets():
                item_to_remove = self.arms
                self.arms = None
            case Trousers():
                item_to_remove = self.legs
                self.legs = None
            case Boots():
                item_to_remove = self.feet
                self.feet = None
        if item_to_remove is None:
            print("No item is equipped, cannot discard it")
        return item_to_remove

    def get_item_parameters(self, currently_equipped_item: Armour | None) -> int | None:
        match currently_equipped_item:
            case Helmet():
                currently_equipped_item = self.head
            case Breastplate():
                currently_equipped_item = self.torso
            case Gauntlets():
                currently_equipped_item = self.arms
            case Trousers():
                currently_equipped_item = self.legs
            case Boots():
                currently_equipped_item = self.feet
        if currently_equipped_item is None:
            print("This body part is not armored. You must be really brave for going at monsters like that!")
            return None
        return currently_equipped_item.item_parameters

    def view_equipped_items(self) -> ItemsView[str, Armour | None]:
        return self.armor_slots.items()


# Константные переменные в питоне записываются полностью большими буквами, как в примере с
# INITIAL_PLAYER_INVENTORY
