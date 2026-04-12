import random
from typing import Self

from game_files.entities.entity import Entity


class DamageDealingEntity(Entity):
    def deal_damage(self, character_taking_damage: Entity) -> None:
        if not self.alive:
            return
        character_taking_damage.health_points = character_taking_damage.health_points - self.damage
        print(
            character_taking_damage.name
            + " gets hit and screams "
            + random.choice(character_taking_damage.damage_stockphrases)
        )
        if character_taking_damage.health_points <= 0:
            character_taking_damage.alive = False
            character_taking_damage.death(character_taking_damage)
