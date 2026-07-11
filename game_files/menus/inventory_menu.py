from game_files.entities.player import Player
from game_files.mediator_module.mediator_module import inventory_slot_mediator
from game_files.items.usable_item import UsableItem


class InventoryMenu:
    def select_item(self, player_character: Player) -> None:
        item_index = int(input("Please, type the item's index"))
        current_item = player_character.inventory.choose_item(item_index)
        if not current_item:
            print("Item not found, try harder")
            return
        player_command = input(f"""You have picked a {current_item} What would you like to do with it?
    1 - equip the item
    2 - examine the item
    3 - use the item
    4 - return to the main inventory
    """)
        if player_command not in {"1", "2", "3", "4"}:
            print("No such command, try again, dumbass")
        elif player_command == "4":
            return
        elif player_command == "3":
            if not isinstance(current_item, UsableItem):
                print("Cannot use this item, try again, chief")
                return
            item_usability_interface.use_item(player_character, current_item, item_index)
            player_character.inventory.discard_item(item_index)
        elif player_command == "2":
            current_item.chosen_item_examination()
        else:
            inventory_slot_mediator.hand_over_item_to_active_slot(current_item, player_character)

    def move_equipped_item_back_to_inventory(self, player_character: Player) -> None:
        slot_to_remove_item_from = str(
            input("Please, choose the part that you want to remove the item from (i.e. left hand/torso, etc.)")
        )
        if slot_to_remove_item_from not in {"main_hand", "secondary_hand", "head", "torso", "arms", "legs", "feet"}:
            print("No such slot, try harder, chief")
        item_to_remove = getattr(inventory_slot_mediator, slot_to_remove_item_from)
        inventory_slot_mediator.get_item_from_active_slot(item_to_remove, player_character)

    def inventory_navigation(self, player_character: Player) -> None:
        while True:
            inventory_slot_mediator.list_all_items(player_character)
            user_input = input(
                "These are all the items in the inventory. What would you like to do next? "
                "1 - select one of the items, 2 - move an equipped item back to inventory, 3 - return to the main game"
            )
            if user_input not in {"1", "2", "3"}:
                print("No such command, use '1', '2' or '3'")
            elif user_input == "3":
                return
            elif user_input == "2":
                self.move_equipped_item_back_to_inventory(player_character, item_equipment_mechanic)
            else:
                self.select_item(player_character, item_equipment_mechanic)
