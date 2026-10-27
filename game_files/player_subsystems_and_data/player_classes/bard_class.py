import random

from player_subsystems_and_data.player_skill_system.skills.bard_skills.bard_skill_tree import BardSkillTree

from game_files.entities.player import Player


class BardPlayer(Player):
    def __init__(self, given_name: str) -> None:
        super().__init__(given_name, "Bard")
        self.health_points = 60
        self.minimal_damage = 45
        self.maximal_damage = 90
        self.general_damage = random.randint(self.minimal_damage, self.maximal_damage)
        self.strength = 5
        self.magic = 3
        self.endurance = 6
        self.intelligence = 5
        self.perception = 6
        self.dexterity = 6
        self.skill_tree = BardSkillTree()
