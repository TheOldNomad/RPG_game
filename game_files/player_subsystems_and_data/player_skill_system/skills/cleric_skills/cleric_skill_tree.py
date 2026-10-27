from player_subsystems_and_data.player_skill_system.skills.skill import Skill
from player_subsystems_and_data.player_skill_system.skills.skill_tree_template import SkillTreeTemplate

from game_files.entities.player import Player


class ClericSkillTree(SkillTreeTemplate):
    def __init__(self) -> None:
        self.cleric_skill_tree = []

    def view_character_skill_tree(self) -> None:
        print(f"{self.cleric_skill_tree}")

    def choose_skill(self, skill_index: int) -> Skill:
        return self.cleric_skill_tree[skill_index]

    def acquire_skill(self, player: Player, skill_index: int) -> None:
        player.acquired_skills = self.cleric_skill_tree[skill_index]
