from game_files.entities.monster import Monster
from game_files.entities.player import Player


class AttackMediator:
    def compute_player_dealt_damage_to_mob(
        self, player_character: Player, monster_list: list, attacked_monster_index: int
    ) -> None:
        attacked_monster = monster_list[attacked_monster_index]
        active_weapon_damage_points = player_character.weapon_and_armor_slots.get_weapon_parameters()
        monster_defense_points = attacked_monster.weapon_and_armor_slots.get_armor_parameters()
        damage_dealt_by_player = (player_character.damage + active_weapon_damage_points) * monster_defense_points
        player_character.deal_damage(monster_list[attacked_monster_index], damage_dealt_by_player)
        if not monster_list[attacked_monster_index].alive:
            monster_list.pop(attacked_monster_index)

    def compute_mob_dealt_damage_to_player(self, attacking_monster: Monster, player_character: Player) -> None:
        monster_dealt_damage = attacking_monster.weapon_and_armor_slots.get_weapon_parameters()
        player_equipped_armor_points = player_character.weapon_and_armor_slots.get_armor_parameters()
        monster_dealt_damage = (attacking_monster.damage + monster_dealt_damage) * player_equipped_armor_points
