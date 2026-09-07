from game_files.entities.damage_dealing_entity import DamageDealingEntity
from game_files.inventories.player_inventory import Inventory
from game_files.inventories.weapon_and_armor_slots import WeaponAndArmorSlots
from game_files.player_skill_system.skills import skill_tree_menu


class Player(DamageDealingEntity):
    rpg_class: str
    current_level: int
    experience_points: int

    def __init__(self, given_name: str, given_rpg_class: str):
        self.name = given_name
        self.rpg_class = given_rpg_class
        self.current_level = 1
        self.experience_points = 0
        self.alive = True
        self.damage_stockphrases = ["Motherfucker", "Uuu suka", "You wanker", "Fuck, I'm bleeding"]
        self.death_stockphrases = ["Uuu suka", "I'm seeing stars...", "Bratan, this is fiasco", "I will meet Reagan.."]
        self.acquired_skills = []
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
        if self.current_level / 2:
            skill_tree_menu.pick_new_skill()
