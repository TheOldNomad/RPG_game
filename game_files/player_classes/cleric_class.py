import random

from game_files.entities.player import Player
from game_files.player_skill_system.skills.cleric_skills.cleric_skill_tree import ClericSkillTree


class ClericPlayer(Player):
    def __init__(self, given_name: str) -> None:
        super().__init__(given_name, "Cleric")
        self.health_points = 40
        self.minimal_damage = 30
        self.maximal_damage = 60
        self.general_damage = random.randint(self.minimal_damage, self.maximal_damage)
        self.strength = 4
        self.magic = 7
        self.endurance = 5
        self.intelligence = 7
        self.perception = 6
        self.dexterity = 5
        self.skill_tree = ClericSkillTree()
