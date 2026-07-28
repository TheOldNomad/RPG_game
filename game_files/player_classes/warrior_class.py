from game_files.entities.player import Player

class WarriorPlayer(Player):
    def __init__(self) -> None:
        super.()_init(self)
        self.rpg_class = "Warrior"
        self.health_points = 60
        self.minimal_damage = 45
        self.maximal_damage = 90
        self.general_damage = random.randint(self.minimal_damage, self.maximal_damage)