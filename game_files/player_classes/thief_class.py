from game_files.entities.player import Player

class ThiefPlayer(Player):
    def __init__(self) -> None:
        super.()_init(self)
        self.rpg_class = "Thief"
        self.health_points = 50
        self.minimal_damage = 35
        self.maximal_damage = 75
        self.general_damage = random.randint(self.minimal_damage, self.maximal_damage)