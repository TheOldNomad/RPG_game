import random

from game_files.items.items import Item


class Armor(Item):
    armor_points: int
    slot_to_equip: str


class Helmet(Armor):
    def __init__(self, key_name: str) -> None:
        self.item_type = "Armour"
        self.item_name = key_name
        self.item_description = "Made to protect that "
        self.slot_to_equip = "Head"
        self.armor_points = random.randint(10, 20)


class Breastplate(Armor):
    def __init__(self, key_name: str) -> None:
        self.item_type = "Armour"
        self.item_name = key_name
        self.item_description = "Made to protect that "
        self.slot_to_equip = "Torso"
        self.armor_points = random.randint(40, 60)


class Gauntlets(Armor):
    def __init__(self, key_name: str) -> None:
        self.item_type = "Armour"
        self.item_name = key_name
        self.item_description = "Made to protect that "
        self.slot_to_equip = "Hands"
        self.armor_points = random.randint(5, 10)


class Trousers(Armor):
    def __init__(self, key_name: str) -> None:
        self.item_type = "Armour"
        self.item_name = key_name
        self.item_description = "Made to protect that "
        self.slot_to_equip = "Legs"
        self.armor_points = random.randint(20, 40)


class Boots(Armor):
    def __init__(self, key_name: str) -> None:
        self.item_type = "Armour"
        self.item_name = key_name
        self.item_description = "Made to protect that "
        self.slot_to_equip = "Feet"
        self.armor_points = random.randint(10, 15)
