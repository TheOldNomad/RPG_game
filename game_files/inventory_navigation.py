from .player_character_inventory import AdvancedPotion, Axe, Potion, Sword

inventory = {
    "item 1": Sword("Faggot slayer"),
    "item 2": Axe("N-word crusher"),
    "item 3": Potion("Baltica 9"),
    "item 4": AdvancedPotion("Okhota Krepkaya"),
}


def list_all_items() -> None:
    for item_id, current_item in inventory.items():
        print(item_id, current_item)


def choosing_item() -> None:
    item_id = input("Please, type the item's id")
    current_item = inventory.get(item_id)
    if current_item:
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
            current_item.equip_item()
    else:
        print("Item not found, try harder")


def inventory_navigation() -> None:
    while True:
        user_input = input("""Please, choose a command:
1 - open the inventory
2 - return to the main game
""")
        if user_input not in {"1", "2"}:
            print("No such command, try again, dumbass")
        elif user_input == "2":
            return
        else:
            list_all_items()
            secondary_input = input("These are all the items in the inventory. Would you like to equip one of them?")
            if secondary_input not in {"Yes", "No"}:
                print("No such command, use 'Yes' or 'No'")
            elif secondary_input == "No":
                return
            else:
                choosing_item()
