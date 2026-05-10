import random
from abc import ABC, abstractmethod


class Item(ABC):
    item_name: str
    item_description: str
    item_parameters: int
    item_type: str

    def chosen_item_examination(self) -> None:
        print(
            f"You are looking at '{self.item_name}', "
            f"which is a {self.item_type}. "
            f"It is {self.item_description}."
            f"{self.item_parameters}."
        )

    def __str__(self) -> str:
        return f"{self.item_type}: {self.item_name}"


class Weapon(Item):
    damage_dealt: int
    weapon_type: str
    hand_to_equip: str


class MainWeapon(Weapon):
    pass


class SecondaryWeapon(Weapon):
    pass


class OneHandedMainWeapon(MainWeapon):
    pass


class TwoHandedMainWeapon(MainWeapon):
    pass


class OneHandedSecondaryWeapon(SecondaryWeapon):
    pass
    

class Sword(OneHandedMainWeapon):
    def __init__(self, key_name: str) -> None:
        self.item_type = "Weapon"
        self.item_name = key_name
        self.item_description = """a weapon from much more elegant times, built for slaying the enemies of the state. "
        Its damage is """
        self.hand_to_equip = "main hand"
        self.item_parameters = self.damage_dealt = random.randint(45, 90)


class Axe(OneHandedMainWeapon):
    def __init__(self, key_name: str) -> None:
        self.item_type = "Weapon"
        self.item_name = key_name
        self.item_description = """a weapon from much more barbaric times, built for slaying you-know-who.
        "Its damage is """
        self.hand_to_equip = "main hand"
        self.item_parameters = self.damage_dealt = random.randint(60, 120)


class Dagger(OneHandedSecondaryWeapon):
    def __init__(self, key_name: str) -> None:
        self.item_type = "Weapon"
        self.item_name = key_name
        self.item_description = """a weapon from much more barbaric times, built for slaying you-know-who.
        "Its damage is """
        self.hand_to_equip = "secondary hand"
        self.item_parameters = self.damage_dealt = random.randint(20, 40)


class Club(OneHandedSecondaryWeapon):
    def __init__(self, key_name: str) -> None:
        self.item_type = "Weapon"
        self.item_name = key_name
        self.item_description = """a weapon from much more barbaric times, built for slaying you-know-who.
        "Its damage is """
        self.hand_to_equip = "secondary hand"
        self.item_parameters = self.damage_dealt = random.randint(20, 40)


class Potion(Item):
    health_restoration: int

    @abstractmethod
    def __init__(self, key_name: str) -> None:
        pass


class HealthPotion(Potion):
    def __init__(self, key_name: str) -> None:
        self.item_type = "Health potion"
        self.item_name = key_name
        self.item_description = (
            "a potion, brewed by the madliest of alchemists, determined to create the ultimate decoction for healing. "
            "The number of hp it restores is"
        )
        self.item_parameters = self.health_restoration = 30


class AdvancedHealthPotion(Potion):
    def __init__(self, key_name: str) -> None:
        self.item_type = "Health potion"
        self.item_name = key_name
        self.item_description = (
            "a potion, brewed by the madliest of alchemists, fancied in particular by the Montenegrian hunters. "
            "The number of hp it restores is"
        )
        self.item_parameters = self.health_restoration = 50


class Armour(Item):
    armour_points: int
    slot_to_equip: str


class Helmet(Armour):
    def __init__(self, key_name: str) -> None:
        self.item_type = "Armour"
        self.item_name = key_name
        self.item_description = "Made to protect that "
        self.slot_to_equip = "Head"


class Breastplate(Armour):
    def __init__(self, key_name: str) -> None:
        self.item_type = "Armour"
        self.item_name = key_name
        self.item_description = "Made to protect that "
        self.slot_to_equip = "Torso"


class Gauntlets(Armour):
    def __init__(self, key_name: str) -> None:
        self.item_type = "Armour"
        self.item_name = key_name
        self.item_description = "Made to protect that "
        self.slot_to_equip = "Hands"


class Trousers(Armour):
    def __init__(self, key_name: str) -> None:
        self.item_type = "Armour"
        self.item_name = key_name
        self.item_description = "Made to protect that "
        self.slot_to_equip = "Legs"


class Boots(Armour):
    def __init__(self, key_name: str) -> None:
        self.item_type = "Armour"
        self.item_name = key_name
        self.item_description = "Made to protect that "
        self.slot_to_equip = "Feet"


# Написать отдельный параметр для брони, который будет int и будет указывать процент защиты
