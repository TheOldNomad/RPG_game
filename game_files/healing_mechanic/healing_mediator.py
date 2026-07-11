from game_files.entities.damage_dealing_entity import DamageDealingEntity
from game_files.items.potions import HealthPotion


class HealingMediator:
    def use_health_potion(
        self, entity_to_use_potion: DamageDealingEntity, potion_to_use: HealthPotion, hp_to_regenerate: int) -> None:
        entity_to_use_potion.healing(entity_to_use_potion, hp_to_regenerate)
