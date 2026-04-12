from game_files.items_and_inventories.item_equipper import ItemEquipper
from game_files.items_and_inventories.player_inventory import ArmorSlots, Inventory, WeaponSlots
from game_files.menus.active_slot_menu import ActiveSlotMenu
from game_files.menus.inventory_and_active_slots_mediator import InventoryAndActionSlotsMediator


class InventoryMenu:
    def select_item(self, inventory: Inventory, weapon_slots: WeaponSlots, armor_slots: ArmorSlots) -> None:
        item_index = int(input("Please, type the item's index"))
        item_type_check = ItemEquipper()
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

    def inventory_navigation(
        self, player_inventory: Inventory, weapon_slots: WeaponSlots, armor_slots: ArmorSlots, active_slot_menu: ActiveSlotMenu, inventory_mediator: InventoryAndActionSlotsMediator
) -> None:
        while True:
            inventory_mediator.list_all_items_in_inventory()
            user_input = input(
                "These are all the items in the inventory. What would you like to do next? 1 - equip one of the items, 2 - see the currently equipped items, 3 - return to the main game"
            )
            if user_input not in {"1", "2", "3"}:
                print("No such command, use '1', '2' or '3'")
            elif user_input == "3":
                return
            elif user_input == "2":
                active_slot_menu.view_currently_equipped_items()
            else:
                self.select_item(player_inventory, weapon_slots, armor_slots)
