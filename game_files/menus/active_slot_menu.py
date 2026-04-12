from game_files.items_and_inventories.player_inventory import ActiveSlots


class ActiveSlotMenu:
    def active_slots_navigation(self, weapon_slots: ActiveSlots, armor_slots: ActiveSlots) -> None:
        slots_to_view = input("Please, choose the slot you would like to see: 1 - equipped weapons, 2 - equipped armor")
        if slots_to_view not in {"1", "2"}:
            print("No such option, try again")
        else:
            self.view_currently_equipped_items(slots_to_view)

    def view_currently_equipped_items(self, slots_to_view: str, weapon_slots: ActiveSlots, armor_slots: ActiveSlots) -> None:
        if slots_to_view == "1":
            armor_slots.view_equipped_items
        if slots_to_view == "2":
            weapon_slots.view_equipped_items

