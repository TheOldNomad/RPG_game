import random
from game_files.entities.player import Player

class MagePlayer(Player):
    def __init__(self, given_name: str) -> None:
        super.()_init(given_name: str, "Mage")
        self.health_points = 45
        self.minimal_damage = 40
        self.maximal_damage = 80
        self.general_damage = random.randint(self.minimal_damage, self.maximal_damage)