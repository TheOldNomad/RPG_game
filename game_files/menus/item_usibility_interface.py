from game_files.entities.player import Player
from game_files.healing_mechanic.healing_mediator import HealingMediator
from game_files.items.potions import HealthPotion
from game_files.items.usable_item import UsableItem


class ItemUsibilityInterface:
    def use_item(self, player: Player, item_to_use: UsableItem, item_to_use_index: int) -> None:
        healing_mechanic = HealingMediator()
        if isinstance(item_to_use, HealthPotion):
            healing_mechanic.use_health_potion(player, item_to_use, item_to_use_index)
