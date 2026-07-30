from game_files.entities.player import Player

class BardSkillTree:
    def __init__(self):
        self.bard_skill_tree = []

    def view_relevant_skill_tree(self, player: Player) -> None:
        print(f"{self.bard_skill_tree}")

    def acquire_skill(self, player: Player, skill_index: int) -> None:
        player.acquired_skills = self.bard_skill_tree[skill_index]