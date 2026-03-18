from items.player_inventory import Inventory


class ItemPickUp:
    def choose_item_to_pick_up(self, item_choice_menu: list) -> None:
        item_choice_menu = []
        items_to_add = []
        user_choice = input(
            f"""Here are the items -"""
            f"""enumerate({item_choice_menu}, start = 1) What would you like to do?
                            1 - take one item,
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
                item_index = int(input("Enter the index of the item you want to pick up"))
                for current_index, current_item in enumerate(item_choice_menu, start=1):
                    if item_index == current_index:
                        items_to_add.append(item_choice_menu.pop(item_index - 1(current_item)))
                return
        else:
            print("No such option. Try again, dumbass")
            return

    def open_item_menu(self, item_list: list, player_inventory: Inventory) -> None:
        player_inventory.add_item(item_list)
