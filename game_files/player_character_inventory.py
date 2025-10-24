import random

from .items import Item


class Sword(Item):
    def __init__(self) -> None:
        self.item_type = "Weapon"
        self.item_name = "Faggot slayer"
        self.item_description = "A weapon from much more elegant times, built for slaying the enemies of the state"
        self.item_parameters = random.randint(45, 90)


class Axe(Item):
    def __init__(self) -> None:
        self.item_type = "Weapon"
        self.item_name = "N-word crusher"
        self.item_description = "A weapon from much more barbaric times, built for slaying you-know-who"
        self.item_parameters = random.randint(60, 120)


class Potion(Item):
    def __init__(self) -> None:
        self.item_type = "Health potion"
        self.item_name = "Baltica 9"
        self.item_description = (
            "A potion, brewed by the madliest of alchemists, determined to create the ultimate decoction for healing"
        )
        self.item_parameters = 30


class AdvancedPotion(Item):
    def __init__(self) -> None:
        self.item_type = "Health potion"
        self.item_name = "Okhota Krepkaya"
        self.item_description = (
            "A potion, brewed by the madliest of alchemists, fancied in particular by the Montenegrian hunters"
        )
        self.item_parameters = 50


inventory = {
    "item 1": Sword("Faggot slayer"),
    "item 2": Axe("N-word crusher"),
    "item 3": Potion("Baltica 9"),
    "item 4": AdvancedPotion("Okhota Krepkaya"),
}


def list_all_items() -> None:
    for item_id, current_item in inventory.items():
        print(f"{item_id.name()}: {current_item}")


def inventory_navigation() -> None:
    user_input = input("""Please, choose a command:
1 - open the inventory
2 - examine the item
""")
    while True:
        if user_input == "1":
            list_all_items(inventory)
            print("These are all the items in the inventory. Would you like to equip one of them?")
            if user_input != "Yes" or user_input != "No":
                print("No such command, use 'Yes' or 'No'")
            elif user_input != "No":
                return
            else:
                print("Please, type the item's id to equip it")
                # equip


# В данном файле потенциально прописать все объекты класса Item, которые пойдут в массив player_character_inventory
# Предложение от Бимбо - написать while-loop в этой вкладке для навигации по инвентарю; таким образом, чтобы в главном
# меню помимо выбора монстра для нападения, была опция с открытием инвентаря.
