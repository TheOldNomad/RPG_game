from game_files.entities.player import Player
from game_files.items.items import Item
from game_files.items.player_inventory import Inventory


def list_all_items(player: Player) -> None:
    if not player.inventory:
        print("The inventory is currently empty")
        return
    for item_id, current_item in player.inventory.items():
        print(item_id, current_item)


def choose_item(item_id: str, inventory: Inventory) -> Item | None:
    return inventory.choose_item(item_id)


def select_item(inventory: Inventory) -> None:
    item_id = input("Please, type the item's id")
    current_item = inventory.choose_item(item_id)
    if not current_item:
        print("Item not found, try harder")
        return

    player_command = input(f"""You have picked a {current_item} What would you like to do with it?
1 - equip the item
2 - examine the item
3 - return to the main inventory
""")
    if player_command not in {"1", "2", "3"}:
        print("No such command, try again, dumbass")
    elif player_command == "3":
        return
    elif player_command == "2":
        current_item.chosen_item_examination()
    else:
        inventory.add_item(current_item)


# def list_commands ():
# commands = []
# while True:
#         print("Please, choose a command:")
#         for number, c in enumerate(commands, 1):
#             print(f"{}- {c}")


def inventory_navigation(player: Player) -> None:
    while True:
        user_input = input("""Please, choose a command:
    1 - open the inventory
    2 - return to the main game
    """)
        if user_input not in {"1", "2"}:
            print("No such command, try again, dumbass")
            continue
        if user_input == "2":
            return
        match input():
            case "1":
                list_all_items(player)
                secondary_input = input(
                    "These are all the items in the inventory. Would you like to equip one of them?"
                )
                if secondary_input not in {"Yes", "No"}:
                    print("No such command, use 'Yes' or 'No'")
                elif secondary_input == "No":
                    return
                else:
                    select_item(player)
            case "2":
                return
            case _:
                print("No such command, try again, dumbass")


def introductory_choice(player: Player, encountered_mobs: list) -> None:
    player_choice = input("""You see a suspiciously looking cave. What will be your actions?" \
        "1 - open the inventory" \
        "2 - enter the cave""")
    if player_choice not in {"1", "2"}:
        print("No such option exists, try again, smartass")
    elif player_choice == "1":
        inventory_navigation(player)
    else:
        player.choose_target_to_attack(encountered_mobs)
