from abc import abstractmethod

from game_files.items.items import Item


class ActiveCombatItem(Item):
    level_required: int

    @abstractmethod
    def __init__(self) -> None:
        pass
