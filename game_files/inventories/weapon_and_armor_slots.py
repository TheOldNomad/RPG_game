from game_files.items.armor import Armor, Boots, Breastplate, Gauntlets, Helmet, Trousers
from game_files.items.weapons import OneHandedMainWeapon, OneHandedSecondaryWeapon, Weapon


class WeaponAndArmorSlots:
    def __init__(self) -> None:
        self.main_hand: OneHandedMainWeapon | None = None
        self.secondary_hand: OneHandedSecondaryWeapon | None = None
        self.head: Helmet | None = None
        self.torso: Breastplate | None = None
        self.arms: Gauntlets | None = None
        self.legs: Trousers | None = None
        self.feet: Boots | None = None

    def equip_item(self, item_to_equip: Weapon | Armor) -> None:
        match item_to_equip:
            case OneHandedMainWeapon():
                if self.main_hand is not None:
                    self.discard_item(self.main_hand)
                self.main_hand = item_to_equip
            case OneHandedSecondaryWeapon():
                if self.secondary_hand is not None:
                    self.discard_item(self.secondary_hand)
                self.secondary_hand = item_to_equip
            case Helmet():
                if self.head is not None:
                    self.discard_item(self.head)
                self.head = item_to_equip
            case Breastplate():
                if self.torso is not None:
                    self.discard_item(self.torso)
                self.torso = item_to_equip
            case Gauntlets():
                if self.arms is not None:
                    self.discard_item(self.arms)
                self.arms = item_to_equip
            case Trousers():
                if self.legs is not None:
                    self.discard_item(self.legs)
                self.legs = item_to_equip
            case Boots():
                if self.feet is not None:
                    self.discard_item(self.feet)
                self.feet = item_to_equip
            case _:
                print("Wrong item type, dumbass, try again")

    def discard_item(self, item_to_remove: Weapon | Armor | None) -> Weapon | Armor | None:
        item_returned_to_inventory = None
        if item_to_remove is None:
            print("No item is equipped, cannot discard it")
            return None
        match item_to_remove:
            case OneHandedMainWeapon():
                item_returned_to_inventory = self.main_hand
                self.main_hand = None
            case OneHandedSecondaryWeapon():
                item_returned_to_inventory = self.secondary_hand
                self.secondary_hand = None
            case Helmet():
                item_returned_to_inventory = self.head
                self.head = None
            case Breastplate():
                item_returned_to_inventory = self.torso
                self.torso = None
            case Gauntlets():
                item_returned_to_inventory = self.arms
                self.arms = None
            case Trousers():
                item_returned_to_inventory = self.legs
                self.legs = None
            case Boots():
                item_returned_to_inventory = self.feet
                self.feet = None
            case _:
                print("Wrong item type")
        return item_returned_to_inventory

    def get_weapon_parameters(self) -> int:
        if self.main_hand is None:
            return 0
        return self.main_hand.item_parameters

    def get_armor_parameters(self) -> float:
        all_equipped_armor: list[Armor | None] = [self.head, self.torso, self.arms, self.legs, self.feet]
        return sum(armor_part.armor_points for armor_part in all_equipped_armor if armor_part is not None) / 100

    def view_equipped_items(self) -> str | Weapon | Armor | None:
        print(f"{self.__dict__.items()}")
