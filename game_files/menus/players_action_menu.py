from menus.player_attack_menu import PlayerAttackMenu

from game_files.entities.player import Player
from game_files.menus.inventory_menu import InventoryMenu


class PlayersActionMenu:
    def introductory_choice(self, monster_list: list, active_player: Player) -> None:
        inventory_interface = InventoryMenu()
        attack_menu = PlayerAttackMenu()
        player_choice = input("""You see a suspiciously looking cave. What will be your actions?" \
            "1 - open the inventory" \
            "2 - enter the cave""")
        if player_choice not in {"1", "2"}:
            print("No such option exists, try again, smartass")
        elif player_choice == "1":
            inventory_interface.inventory_navigation(
                active_player.inventory,
                active_player.weapon_and_armor_slots,
                active_player.item_equipment_mechanic,
            )
        else:
            attack_menu.choose_target_to_attack(monster_list, active_player)
