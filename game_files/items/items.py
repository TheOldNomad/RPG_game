import random


class Item:
    item_type: str
    item_name: str
    item_description: str
    item_parameters: int

    def chosen_item_examination(self) -> None:
        print(
            f"You are looking at '{self.item_name}', "
            f"which is a {self.item_type}. "
            f"It is {self.item_description}."
            f"{self.item_parameters}."
        )

    def __str__(self) -> str:
        return f"{self.item_type}: {self.item_name}"


class Sword(Item):
    def __init__(self, key_name: str) -> None:
        self.item_type = "Weapon"
        self.item_name = key_name
        self.item_description = """a weapon from much more elegant times, built for slaying the enemies of the state. "
        Its damage is """
        self.item_parameters = self.damage_dealt = random.randint(45, 90)


class Axe(Item):
    def __init__(self, key_name: str) -> None:
        self.item_type = "Weapon"
        self.item_name = key_name
        self.item_description = """a weapon from much more barbaric times, built for slaying you-know-who.
        "Its damage is """
        self.item_parameters = self.damage_dealt = random.randint(60, 120)


class Potion(Item):
    def __init__(self, key_name: str) -> None:
        self.item_type = "Health potion"
        self.item_name = key_name
        self.item_description = (
            "a potion, brewed by the madliest of alchemists, determined to create the ultimate decoction for healing. "
            "The number of hp it restores is"
        )
        self.item_parameters = self.health_restoration = 30


class AdvancedPotion(Item):
    def __init__(self, key_name: str) -> None:
        self.item_type = "Health potion"
        self.item_name = key_name
        self.item_description = (
            "a potion, brewed by the madliest of alchemists, fancied in particular by the Montenegrian hunters. "
            "The number of hp it restores is"
        )
        self.item_parameters = self.health_restoration = 50
