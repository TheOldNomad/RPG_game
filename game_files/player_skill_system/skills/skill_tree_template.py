from __future__ import annotations

from typing import TYPE_CHECKING

from game_files.player_skill_system.skills.skill import Skill

if TYPE_CHECKING:
    from game_files.entities.player import Player


class SkillTreeTemplate:
    def __init__(self) -> None:
        self.skill_tree = []

    def view_character_skill_tree(self) -> None:
        print(f"{self.skill_tree}")

    def choose_skill(self, skill_index: int) -> Skill:
        return self.skill_tree[skill_index]

    def acquire_skill(self, player: Player, skill_index: int) -> None:
        player.acquired_skills = self.skill_tree[skill_index]
