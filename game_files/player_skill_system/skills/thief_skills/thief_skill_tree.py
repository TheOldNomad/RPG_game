from game_files.entities.player import Player
from game_files.player_skill_system.skills.skill import Skill
from game_files.player_skill_system.skills.skill_tree_template import SkillTreeTemplate


class ThiefSkillTree(SkillTreeTemplate):
    def __init__(self) -> None:
        self.thief_skill_tree = []

    def view_character_skill_tree(self) -> None:
        print(f"{self.thief_skill_tree}")

    def choose_skill(self, skill_index: int) -> Skill:
        return self.thief_skill_tree[skill_index]

    def acquire_skill(self, player: Player, skill_index: int) -> None:
        player.acquired_skills = self.thief_skill_tree[skill_index]
