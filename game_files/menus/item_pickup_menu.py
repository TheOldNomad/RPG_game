from game_files.inventories.player_inventory import Inventory
from game_files.items.items import Item


class ItemPickUpMenu:
    def choose_item_to_pick_up(self, encountered_items_list: list, player_inventory: Inventory) -> None:
        items_to_add = []
        user_choice = input(
            f"""Here are the items -"""
            f"""enumerate({encountered_items_list}, start = 1) What would you like to do?
                            1 - take one item,
                            2 - take some items,
                            3 - take all the items,
                            4 - close the menu"""
        )
        if user_choice == "4":
            return
        if user_choice == "3":
            items_to_add.extend(encountered_items_list)
            encountered_items_list.clear()
            return
        if user_choice == "2":
            while True:
                chosen_items_indexes_row = input(
                    "Enter the indexes of the items you would like to pick up, separate them using spacebar"
                )
                item_choice_menu_indexes = [int(index) for index in chosen_items_indexes_row.split()]
                print(item_choice_menu_indexes)
                for current_index in item_choice_menu_indexes:
                    items_to_add.extend(encountered_items_list.pop(current_index))
                    self.hand_multiple_items_to_inventory(items_to_add, player_inventory)
                return
        if user_choice == "1":
            chosen_item_index = int(input("Enter the indexes of the item you would like to pick up"))
            item_to_add = encountered_items_list[chosen_item_index]
            self.hand_one_item_to_inventory(item_to_add, player_inventory)
        else:
            print("No such option. Try again, dumbass")
            return

    def hand_one_item_to_inventory(self, item_to_add: Item, player_inventory: Inventory) -> None:
        player_inventory.add_item(item_to_add)
        print(f"{item_to_add} successfully added to inventory!")

    def hand_multiple_items_to_inventory(self, items_to_add: list, player_inventory: Inventory) -> None:
        player_inventory.add_multiple_items(items_to_add)
        print(f"{items_to_add} successfully added to inventory!")
