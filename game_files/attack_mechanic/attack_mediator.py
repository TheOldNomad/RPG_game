from game_files.inventories.weapon_and_armor_slots import WeaponAndArmorSlots
from game_files.entities.damage_dealing_entity import DamageDealingEntity
from game_files.entities.player import Player
import random

class AttackMediator:
    def compute_player_dealt_damage_to_mob(self, player_character: Player, currently_equipped_weapons: WeaponAndArmorSlots, attacked_monster_index: int) -> int:
        active_weapon_damage_points = currently_equipped_weapons.get_item_parameters
        damage_dealt_by_player = (player_character.damage + active_weapon_damage_points) * 100%
        player_character.deal_damage(monster_list[attacked_monster_index], damage_dealt_by_player)
        if not monster_list[attacked_monster_index].alive:
            monster_list.pop(attacked_monster_index)
