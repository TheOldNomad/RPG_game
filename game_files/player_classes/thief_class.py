import random

from player_skill_system.skills.thief_skills.thief_skill_tree import ThiefSkillTree

from game_files.entities.player import Player


class ThiefPlayer(Player):
    def __init__(self, given_name: str) -> None:
        super().__init__(given_name, "Thief")
        self.health_points = 50
        self.minimal_damage = 35
        self.maximal_damage = 75
        self.general_damage = random.randint(self.minimal_damage, self.maximal_damage)
        self.skill_tree = ThiefSkillTree()
