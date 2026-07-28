from game_files.entities.player import Player

class MagePlayer(Player):
    def __init__(self) -> None:
        super.()_init(self)
        self.rpg_class = "Mage"
        self.health_points = 45
        self.minimal_damage = 40
        self.maximal_damage = 80
        self.general_damage = random.randint(self.minimal_damage, self.maximal_damage)