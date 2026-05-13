from abc import abstractmethod

from game_files.items.items import Item


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
