import random
from typing import Self


class Entity:
    name: str
    health_points: int
    damage: int
    health_regeneration: int
    damage_stockphrases: list[str]
    death_stockphrases: list[str]
    alive: bool

    def death(self, dying_character: Self) -> None:
        print(dying_character.name + " perishes, saying " + random.choice(dying_character.death_stockphrases))
