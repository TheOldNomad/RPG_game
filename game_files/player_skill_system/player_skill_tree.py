from game_files.entities.player import Player

class SkillTree:
    def __init__(self) -> None:
        self.skill_tree = []

    def pick_new_skill(self, player: Player) -> None:
