from game_files.attack_mechanic import player_attack_menu
from game_files.entities.player import Player
from game_files.inventories import inventory_menu


def introductory_choice(monster_list: list, active_player: Player) -> None:
    while active_player.alive:
        player_choice = input(
            "You see a suspiciously looking cave. What will be your actions?\n"
            "1 - open the inventory\n"
            "2 - enter the cave\n"
        )
        if player_choice not in {"1", "2"}:
            print("No such option exists, try again, smartass")
        elif player_choice == "1":
            inventory_menu.inventory_navigation(
                active_player,
            )
            continue
        else:
            player_attack_menu.choose_target_to_attack(monster_list, active_player)
            return
