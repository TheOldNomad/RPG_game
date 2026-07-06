import random

from game_files.entities.damage_dealing_entity import DamageDealingEntity
from game_files.inventories.player_inventory import Inventory
from game_files.inventories.weapon_and_armor_slots import WeaponAndArmorSlots


class Player(DamageDealingEntity):
    rpg_class: str
    current_level: int
    experience_points: int

    def __init__(self, given_name: str, given_rpg_class: str):
        self.name = given_name
        self.rpg_class = given_rpg_class
        self.current_level = 1
        self.health_points = 60
        self.experience_points = 0
        self.minimal_damage = 45
        self.maximal_damage = 90
        self.general_damage = random.randint(self.minimal_damage, self.maximal_damage)
        self.alive = True
        self.damage_stockphrases = ["Motherfucker", "Uuu suka", "You wanker", "Fuck, I'm bleeding"]
        self.death_stockphrases = ["Uuu suka", "I'm seeing stars...", "Bratan, this is fiasco", "I will meet Reagan.."]
        self.weapon_and_armor_slots = WeaponAndArmorSlots()
        self.inventory = Inventory()

    def see_player_state(self) -> None:
        print(
            f"{self.name}\n {self.rpg_class}\n Level {self.current_level}\n Experience {self.experience_points}/1000\n \
              Health points {self.health_points}"
        )

    def gain_experience_points(self, gained_xp: int) -> None:
        self.experience_points += gained_xp
        if self.experience_points >= 1000:
            self.experience_points -= 1000
            self.level_up()

    def level_up(self) -> None:
        self.current_level += 1
        self.minimal_damage += 5
        self.maximal_damage += 5
