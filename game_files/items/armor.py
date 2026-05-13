from game_files.items_and_inventories.items import Item


class Armor(Item):
    armour_points: int
    slot_to_equip: str


class Helmet(Armor):
    def __init__(self, key_name: str) -> None:
        self.item_type = "Armour"
        self.item_name = key_name
        self.item_description = "Made to protect that "
        self.slot_to_equip = "Head"


class Breastplate(Armor):
    def __init__(self, key_name: str) -> None:
        self.item_type = "Armour"
        self.item_name = key_name
        self.item_description = "Made to protect that "
        self.slot_to_equip = "Torso"


class Gauntlets(Armor):
    def __init__(self, key_name: str) -> None:
        self.item_type = "Armour"
        self.item_name = key_name
        self.item_description = "Made to protect that "
        self.slot_to_equip = "Hands"


class Trousers(Armor):
    def __init__(self, key_name: str) -> None:
        self.item_type = "Armour"
        self.item_name = key_name
        self.item_description = "Made to protect that "
        self.slot_to_equip = "Legs"


class Boots(Armor):
    def __init__(self, key_name: str) -> None:
        self.item_type = "Armour"
        self.item_name = key_name
        self.item_description = "Made to protect that "
        self.slot_to_equip = "Feet"
