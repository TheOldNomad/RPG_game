import random

from game_files.entities.damage_dealing_entity import DamageDealingEntity


class Monster(DamageDealingEntity):
    def __init__(self, given_name: str):
        self.name = given_name

        self.health_points = 25
        self.damage = random.randint(1, 30)
        self.alive = True
        self.damage_stockphrases = ["How dare you!", "Oi mate, the fook", "I've caught an olive", "You bitch-ass hoe"]
        self.death_stockphrases = ["Aaaaa bilya", "My... popka", "I will meet Margareth Thatcher..."]
