from game_files.items_and_inventories.inventory_slot_mediator import InventoryAndActionSlotsMediator
from game_files.items_and_inventories.player_inventory import ArmorSlots, Inventory, WeaponSlots


class InventoryMenu:
    def select_item(self, inventory: Inventory, weapon_slots: WeaponSlots, armor_slots: ArmorSlots) -> None:
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
            item_type_check.hand_over_item_to_active_slot(current_item, inventory, weapon_slots, armor_slots)

    def remove_item_from_active_slots(
        self, inventory: Inventory, weapon_slots: WeaponSlots, armor_slots: ArmorSlots
    ) -> None:
        item_type_check = InventoryAndActionSlotsMediator()
        item_to_remove = str(
            input("Please, choose the part that you want to remove the item from (i.e. left hand/torso, etc.)")
        )
        item_type_check.remove_item_from_active_slot(item_to_remove, inventory, weapon_slots, armor_slots)

    def inventory_navigation(
        self,
        player_inventory: Inventory,
        weapon_slots: WeaponSlots,
        armor_slots: ArmorSlots,
        inventory_mediator: InventoryAndActionSlotsMediator,
    ) -> None:
        while True:
            inventory_mediator.list_all_items(player_inventory, weapon_slots, armor_slots)
            user_input = input(
                "These are all the items in the inventory. What would you like to do next? 1 - select one of the items, 2 - move an equipped item back to inventory, 3 - return to the main game"
            )
            if user_input not in {"1", "2", "3"}:
                print("No such command, use '1', '2' or '3'")
            elif user_input == "3":
                return
            elif user_input == "2":
                self.remove_item_from_active_slots(player_inventory, weapon_slots, armor_slots)
            else:
                self.select_item(player_inventory, weapon_slots, armor_slots)
