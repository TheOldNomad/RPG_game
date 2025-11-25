from .items import AdvancedPotion, Axe, Potion, Sword


class Inventory:
    def __init__(self) -> None:
        self.INITIAL_PLAYER_INVENTORY: dict = {
            "item 1": Sword("Faggot slayer"),
            "item 2": Axe("N-word crusher"),
            "item 3": Potion("Baltica 9"),
            "item 4": AdvancedPotion("Okhota Krepkaya"),
        }


# Дописать цикл так, чтобы меню стало «интерактивным» — можно открывать инвентарь,
# экипировать предметы и возвращаться без выхода из функции
# Написать повторный цикл, чтобы пользователь мог экипировать несколько предметов за раз
# Как вариант - воспользоваться enum
# Константные переменные в питоне записываются полностью большими буквами, как в примере с
# INITIAL_PLAYER_INVENTORY
