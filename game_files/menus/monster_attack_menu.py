from game_files.attack_mechanic.attack_mediator import AttackMediator
from game_files.entities.monster import Monster
from game_files.entities.player import Player


class MonsterAttackMenu:
    def register_monster_damage(self, player_character: Player, attacking_monster: Monster) -> None:
        attack_mediator = AttackMediator()
        attack_mediator.compute_mob_dealt_damage_to_player(attacking_monster, player_character)
