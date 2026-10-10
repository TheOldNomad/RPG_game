import random

from game_files.entities.player import Player
from game_files.player_skill_system.skills.mage_skills.mage_skill_tree import MageSkillTree


class MagePlayer(Player):
    def __init__(self, given_name: str) -> None:
        super().__init__(given_name, "Mage")
        self.health_points = 45
        self.minimal_damage = 40
        self.maximal_damage = 80
        self.general_damage = random.randint(self.minimal_damage, self.maximal_damage)
        self.strength = 3
        self.magic = 7
        self.endurance = 4
        self.intelligence = 8
        self.perception = 7
        self.dexterity = 4
        self.skill_tree = MageSkillTree()
