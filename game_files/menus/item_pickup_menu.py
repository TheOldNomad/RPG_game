from game_files.items_and_inventories.player_inventory import Inventory


class ItemPickUpMenu:
    def choose_item_to_pick_up(self, item_choice_menu: list) -> None:
        items_to_add = []
        user_choice = input(
            f"""Here are the items -"""
            f"""enumerate({item_choice_menu}, start = 1) What would you like to do?
                            1 - take certain items,
                            2 - take all items,
                            3 - close the menu"""
        )
        if user_choice == "3":
            return
        if user_choice == "2":
            items_to_add.extend(item_choice_menu)
            item_choice_menu.clear()
            return
        if user_choice == "1":
            while True:
                chosen_items_indexes = int(
                    input("Enter the indexes of the items you would like to pick up, separate them using spacebar")
                )
                items_to_pick_up = [int(index) for index in chosen_items_indexes.split()]
                print(items_to_pick_up)
                for current_index, current_item in enumerate(item_choice_menu, start=1):
                    if (current_index in chosen_items_indexes) and (current_item in chosen_items_indexes):
                        items_to_add.append(item_choice_menu.pop(current_item))
                return
        else:
            print("No such option. Try again, dumbass")
            return

    def open_item_menu(self, item_list: list, player_inventory: Inventory) -> None:
        player_inventory.add_item(item_list)
