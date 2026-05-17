import random

from game_files.items.items import Item


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
