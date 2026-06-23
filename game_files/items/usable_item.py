from abc import abstractmethod

from game_files.items.items import Item
from game_files.entities.damage_dealing_entity import DamageDealingEntity


class UsableItem(Item):
    @abstractmethod
    def item_usability(self, character_to_use_item: DamageDealingEntity) -> None:
        pass
