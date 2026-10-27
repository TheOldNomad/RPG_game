from player_subsystems_and_data.player_skill_system.skills.skill import Skill
from player_subsystems_and_data.player_skill_system.skills.skill_tree_template import SkillTreeTemplate

from game_files.entities.player import Player


class WarriorSkillTree(SkillTreeTemplate):
    def __init__(self) -> None:
        self.warrior_skill_tree = []

    def view_character_skill_tree(self) -> None:
        print(f"{self.warrior_skill_tree}")

    def choose_skill(self, skill_index: int) -> Skill:
        return self.warrior_skill_tree[skill_index]

    def acquire_skill(self, player: Player, skill_index: int) -> None:
        player.acquired_skills = self.warrior_skill_tree[skill_index]
