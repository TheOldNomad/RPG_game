from game_files.entities.damage_dealing_entity import DamageDealingEntity


def use_health_potion(entity_to_use_potion: DamageDealingEntity, hp_to_regenerate: int) -> None:
    entity_to_use_potion.healing(entity_to_use_potion, hp_to_regenerate)
