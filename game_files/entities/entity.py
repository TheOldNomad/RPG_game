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

    def healing(self, character_drinking_potion: Self) -> None:
        character_drinking_potion.health_points = character_drinking_potion.health_points + self.health_regeneration
        print("A sip from the rusty canteen restores your breath and fills you with a nice warmth")
