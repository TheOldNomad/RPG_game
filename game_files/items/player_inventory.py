from .items import AdvancedPotion, Axe, Item, Potion, Sword


class Inventory:
    def __init__(self) -> None:
        self.base_player_inventory: dict = {
            "item 1": Sword("Faggot slayer"),
            "item 2": Axe("N-word crusher"),
            "item 3": Potion("Baltica 9"),
            "item 4": AdvancedPotion("Okhota Krepkaya"),
        }
        self.future_item_id = 1

    def pickup_item(self, picked_up_item: Item) -> str:
        new_id = f"picked_up_item_{self.base_player_inventory}"
        self.base_player_inventory[new_id] = picked_up_item
        self.future_item_id += 1
        return new_id

    def discard_item(self, item_id: str) -> None:
        self.base_player_inventory.pop(item_id)

    def choose_item(self, item_id: str) -> Item | None:
        return self.base_player_inventory.get(item_id)


# Дописать цикл так, чтобы меню стало «интерактивным» — можно открывать инвентарь,
# экипировать предметы и возвращаться без выхода из функции
# Написать повторный цикл, чтобы пользователь мог экипировать несколько предметов за раз
# Как вариант - воспользоваться enum
# Константные переменные в питоне записываются полностью большими буквами, как в примере с
# INITIAL_PLAYER_INVENTORY
