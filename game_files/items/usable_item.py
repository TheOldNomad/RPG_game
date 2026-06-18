from abc import abstractmethod

from game_files.items.items import Item


class UsableItem(Item):
    @abstractmethod
    def use_item(self) -> None:
        pass
