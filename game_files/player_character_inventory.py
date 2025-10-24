from .items import Item


class Sword(Item):
    def __init__(self) -> None:
        self.item_type = "Weapon"
        self.item_name = "Faggot slayer"
        self.item_description = "A weapon from much more elegant times, built for slaying the enemies of the state"
        self.item_parameters = 45, 90


class Potion(Item):
    def __init__(self) -> None:
        self.item_type = "Health potion"
        self.item_name = "Baltica 9"
        self.item_description = (
            "A potion, brewed by the madliest of alchemists, determined to create the ultimate decoction for healing"
        )
        self.item_parameters = 30


# В данном файле потенциально прописать все объекты класса Item, которые пойдут в массив player_character_inventory
# Предложение от Бимбо - написать while-loop в этой вкладке для навигации по инвентарю; таким образом, чтобы в главном
# меню помимо выбора монстра для нападения, была опция с открытием инвентаря.
