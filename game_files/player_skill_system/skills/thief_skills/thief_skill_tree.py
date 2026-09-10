from game_files.entities.player import Player


class ThiefSkillTree:
    def __init__(self) -> None:
        self.thief_skill_tree = []

    def view_relevant_skill_tree(self) -> None:
        print(f"{self.thief_skill_tree}")

    def acquire_skill(self, player: Player, skill_index: int) -> None:
        player.acquired_skills = self.thief_skill_tree[skill_index]
