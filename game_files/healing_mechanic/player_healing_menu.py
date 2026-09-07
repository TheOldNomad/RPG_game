from game_files.entities.player import Player
from game_files.inventories import inventory_menu


def take_health_potion(player_character: Player) -> None:
    user_input = input("Your health seems low. Would you like to drink a potion?1 - Yes2 - No")
    if user_input not in {"1", "2"}:
        print("No such option, use your numpad, genius")
        return
    if user_input == "Yes":
        print("Please, choose the healing potion you would like to take:")
        inventory_menu.inventory_navigation(player_character)
    else:
        return
