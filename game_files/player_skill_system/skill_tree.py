from game_files.entities.player import Player

class SkillTree:
    def __init__(self):
        self.warrior_skill_tree = []
        self.mage_skill_tree = []
        self.thief_skill_tree = []
        self.bard_skill_tree = []
        self.cleric_skill_tree = [] 

    def view_relevant_skill_tree(self, player: Player) -> None:
        match player:
            case Warrior:
                print(f"{self.warrior_skill_tree}")
            case Mage:
                print(f"{self.mage_skill_tree}")
            case Thief:
                print(f"{self.thief_skill_tree}")
            case Bard:
                print(f"{self.bard_skill_tree}")
            case Cleric:
                print(f"{self.cleric_skill_tree}")

    def acquire_skill(self, player: Player, skill_index: int) -> None:
        match player:
            case Warrior:
                player.acquired_skills = self.warrior_skill_tree[skill_index]
            case Mage:
                player.acquired_skills = self.mage_skill_tree[skill_index]
            case Thief:
                player.acquired_skills = self.thief_skill_tree[skill_index]
            case Bard:
                player.acquired_skills = self.bard_skill_tree[skill_index]
            case Cleric:
                player.acquired_skills = self.cleric_skill_tree[skill_index]