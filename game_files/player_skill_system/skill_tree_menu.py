from game_files.entities.player import Player

class SkillTreeMenu:
    def pick_new_skill(self, player: Player) -> None:
        user_input = input("Pick the skill you would like to acquire")
        