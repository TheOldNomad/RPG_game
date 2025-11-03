from .player_character import Player


class Item:
    item_type: str
    item_name: str
    item_description: str
    item_parameters: int

    def chosen_item_examination(self) -> None:
        print(
            f"You are looking at '{self.item_name}', "
            f"which is a {self.item_type}. "
            f"It is {self.item_description}."
            f"It has the following properties: {self.item_parameters}."
        )

    def __str__(self) -> str:
        return f"{self.item_type}: {self.item_name}"

    def equip_item(self, player_character: Player) -> None:
        player_character.active_inventory.append(self)
        print(f"{self} successfully equipped!")
