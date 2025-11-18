import random

from .character import Character


class Monster(Character):
    def __init__(self, given_name: str):
        self.name = given_name

        self.health_points = 25
        self.damage = random.randint(1, 30)
        self.alive = True
        self.damage_stockphrases = ["How dare you!", "Oi mate, the fook", "I've caught an olive", "You bitch-ass hoe"]
        self.death_stockphrases = ["Aaaaa bilya", "My... popka", "I will meet Margareth Thatcher..."]


# self.damage_stockphrases = ["How dare you!", "Oi mate, the fook", "I've caught an olive", "You bitch-ass hoe"]
# self.death_stockphrases = ["Aaaaa bilya", "My... popka", "I will meet Margareth Thatcher..."]
