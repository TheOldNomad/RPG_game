import random

from player_skill_system.skills.cleric_skills.cleric_skill_tree import ClericSkillTree

from game_files.entities.player import Player


class ClericPlayer(Player):
    def __init__(self, given_name: str) -> None:
        super().__init__(given_name, "Cleric")
        self.health_points = 40
        self.minimal_damage = 30
        self.maximal_damage = 60
        self.general_damage = random.randint(self.minimal_damage, self.maximal_damage)
        self.skill_tree = ClericSkillTree()
