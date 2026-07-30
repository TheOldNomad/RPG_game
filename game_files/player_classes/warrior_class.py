import random
from game_files.entities.player import Player

class WarriorPlayer(Player):
    def __init__(self, given_name: str) -> None:
        super.()_init(given_name: str, "Warrior")
        self.health_points = 60
        self.minimal_damage = 45
        self.maximal_damage = 90
        self.general_damage = random.randint(self.minimal_damage, self.maximal_damage)