from game_files.items.usable_item import UsableItem
from game_files.items.potions import HealthPotion
from game_files.healing_mechanic import HealingMediator

class ItemUsibilityInterface:
    def use_item(self, item_to_use: UsableItem, item_to_use_index: int) -> None:
        healing_mechanic = HealingMediator()
        if not isinstance(item_to_use, UsableItem):
            print("Cannot use this item, try again, chief")
            return
        elif isinstance(item_to_use, HealthPotion):
            healing_mechanic.use_health_potion(item_to_use, item_to_use_index)