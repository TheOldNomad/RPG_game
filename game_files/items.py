from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .character import Character


class Item:
    item_type: str
    item_name: str
    item_description: str
    item_parameters: int

    def chosen_item_description(self, character_opening_inventory: "Character") -> None:
        print(
            f"You are looking at '{self.item_name}', "
            f"which is a {self.item_type}. "
            f"It has the following properties: {self.item_parameters}."
        )
