import random

from .items import Item
from .player_character import Player


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


def equip_item(self, player_character: Player) -> None:
    player_character.active_inventory.append(self)
    print(f"{self} successfully equipped!")


# Дописать цикл так, чтобы меню стало «интерактивным» — можно открывать инвентарь,
# экипировать предметы и возвращаться без выхода из функции
# Написать повторный цикл, чтобы пользователь мог экипировать несколько предметов за раз
# Как вариант - воспользоваться enum
