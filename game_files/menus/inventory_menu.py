from game_files.inventories.inventory_slot_mediator import InventoryAndActionSlotsMediator
from game_files.inventories.player_inventory import Inventory
from game_files.inventories.weapon_and_armor_slots import WeaponAndArmorSlots


class InventoryMenu:
    def select_item(self, inventory: Inventory, weapon_and_armor_slots: WeaponAndArmorSlots) -> None:
        item_index = int(input("Please, type the item's index"))
        item_type_check = InventoryAndActionSlotsMediator()
        current_item = inventory.choose_item(item_index)
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
            item_type_check.hand_over_item_to_active_slot(current_item, weapon_and_armor_slots)

    def move_equipped_item_back_to_inventory(
        self, inventory: Inventory, weapon_and_armor_slots: WeaponAndArmorSlots
    ) -> None:
        item_type_check = InventoryAndActionSlotsMediator()
        slot_to_remove_item_from = str(
            input("Please, choose the part that you want to remove the item from (i.e. left hand/torso, etc.)")
        )
        if slot_to_remove_item_from not in {"main_hand", "secondary_hand", "head", "torso", "arms", "legs", "feet"}:
            print("No such slot, try harder, chief")
        item_to_remove = getattr(item_type_check, slot_to_remove_item_from)
        item_type_check.get_item_from_active_slot(item_to_remove, inventory, weapon_and_armor_slots)

    def inventory_navigation(
        self,
        player_inventory: Inventory,
        weapon_and_armor_slots: WeaponAndArmorSlots,
        inventory_mediator: InventoryAndActionSlotsMediator,
    ) -> None:
        while True:
            inventory_mediator.list_all_items(player_inventory, weapon_and_armor_slots)
            user_input = input(
                "These are all the items in the inventory. What would you like to do next? "
                "1 - select one of the items, 2 - move an equipped item back to inventory, 3 - return to the main game"
            )
            if user_input not in {"1", "2", "3"}:
                print("No such command, use '1', '2' or '3'")
            elif user_input == "3":
                return
            elif user_input == "2":
                self.move_equipped_item_back_to_inventory(player_inventory, weapon_and_armor_slots)
            else:
                self.select_item(player_inventory, weapon_and_armor_slots)
