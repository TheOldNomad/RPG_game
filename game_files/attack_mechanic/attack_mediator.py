from game_files.entities.player import Player
from game_files.entities.monster import Monster
from game_files.inventories.weapon_and_armor_slots import WeaponAndArmorSlots
from game_files.items.armor import Armor
from game_files.items.weapons import Weapon


class AttackMediator:
    def compute_player_dealt_damage_to_mob(
        self,
        player_character: Player,
        monster_list: list,
        attacked_monster_index: int,
        item_to_get_parameters_from: Weapon | Armor | None,
    ) -> None:
        active_weapon_damage_points = player_character.weapon_and_armor_slots.get_item_parameters(item_to_get_parameters_from)
        monster_defense_points = 
        if item_to_get_parameters_from is None:
            active_weapon_damage_points = 0
        damage_dealt_by_player = (player_character.damage + active_weapon_damage_points) * currently_equipped_armor_points
        player_character.deal_damage(monster_list[attacked_monster_index], damage_dealt_by_player)
        if not monster_list[attacked_monster_index].alive:
            monster_list.pop(attacked_monster_index)

    def compute_mob_dealt_damage_to_player(self, 
    attacking_monster: Monster, 
    item_to_get_parameters_from: Weapon | Armor | None,
    ) -> None:
        monster_dealt_damage = attacking_monster.weapon_and_armor_slots.get_item_parameters(item_to_get_parameters_from)
        damage_dealt_by_monster = (attacking_monster.damage + monster_dealt_damage) / 100