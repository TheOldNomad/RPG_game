import random
from typing import TYPE_CHECKING

from game_files.items.items import Item
from game_files.items.player_inventory import ActiveInventory, Inventory

from .entity import Entity

if TYPE_CHECKING:
    pass


class Player(Entity):
    rpg_class: str

    def __init__(self, given_name: str, given_rpg_class: str):
        self.name = given_name
        self.rpg_class = given_rpg_class
        self.health_points = 60
        self.damage = random.randint(45, 90)
        self.health_regeneration = 30
        self.alive = True
        self.damage_stockphrases = ["Motherfucker", "Uuu suka", "You wanker", "Fuck, I'm bleeding"]
        self.death_stockphrases = ["Uuu suka", "I'm seeing stars...", "Bratan, this is fiasco", "I will meet Reagan.."]
        self.armor_slots = ActiveInventory()
        self.weapon_slots = ActiveInventory()
        self.inventory = Inventory()

    def choose_target_to_attack(self, encountered_mobs: list) -> None:
        user_input = input("You see monsters, which one do you want to attack? Use the numpad to choose the monster")
        current_monster_index = int(user_input)
        if not user_input.isdigit():
            print("This option is not supported. Use an integer to choose a command")
            return
        if current_monster_index < 0 or current_monster_index >= len(encountered_mobs):
            print("This monster has already perished. Would you like to attack the other one?")
            return
        self.deal_damage(encountered_mobs[current_monster_index])
        if not encountered_mobs[current_monster_index].alive:
            encountered_mobs.pop(current_monster_index)

    def equip_item(self) -> None:
        self.armor_slots.equip_armor()
        print(f"{self} successfully equipped!")


# Вставить сюда проверку, жив ли монстр, если монстр мертв, его нужно удалить из массива с помощью одной из функций
