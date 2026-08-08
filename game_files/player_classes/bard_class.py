import random

from player_skill_system.class_skill_trees.bard_skill_tree import BardSkillTree

from game_files.entities.player import Player


class BardPlayer(Player):
    def __init__(self, given_name: str) -> None:
        super().__init__(given_name, "Bard")
        self.health_points = 60
        self.minimal_damage = 45
        self.maximal_damage = 90
        self.general_damage = random.randint(self.minimal_damage, self.maximal_damage)
        self.skill_tree = BardSkillTree()
