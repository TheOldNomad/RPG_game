import random


class Character:
    name: str
    health_points: int
    damage: int
    health_regeneration: int
    damage_stockphrases: list[str]
    death_stockphrases: list[str]
    alive: bool

    def dealing_damage(self, character_taking_damage: "Character") -> None:
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

    def death(self, dying_character: "Character") -> None:
        print(dying_character.name + " perishes, saying " + random.choice(dying_character.death_stockphrases))

    def healing(self, character_drinking_potion: "Character") -> None:
        character_drinking_potion.health_points = character_drinking_potion.health_points + self.health_regeneration
        print("A sip from the rusty canteen restores your breath and fills you with a nice warmth")
