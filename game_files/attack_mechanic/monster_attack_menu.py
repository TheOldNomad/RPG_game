from game_files.attack_mechanic import attack_mediator
from game_files.entities.monster import Monster
from game_files.entities.player import Player


def register_monster_damage(player_character: Player, attacking_monster: Monster) -> None:
    attack_mediator.compute_mob_dealt_damage_to_player(attacking_monster, player_character)
