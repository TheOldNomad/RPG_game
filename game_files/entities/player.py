import array
import random

from game_files.items.player_inventory import Inventory

from .character import Character


class Player(Character):
    rpg_class: str

    def __init__(self, given_name: str, given_rpg_class: str, base_player_inventory: Inventory):
        self.name = given_name
        self.rpg_class = given_rpg_class
        self.health_points = 60
        self.damage = random.randint(45, 90)
        self.health_regeneration = 30
        self.alive = True
        self.damage_stockphrases = ["Motherfucker", "Uuu suka", "You wanker", "Fuck, I'm bleeding"]
        self.death_stockphrases = ["Uuu suka", "I'm seeing stars...", "Bratan, this is fiasco", "I will meet Reagan.."]
        self.active_inventory = []
        self.inventory = base_player_inventory

    def choose_target_to_attack(self, encountered_mobs: array) -> None:
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

    def equip_item(self, item_id: str) -> None:
        self.active_inventory.append(item_id)
        print(f"{self} successfully equipped!")


# Вставить сюда проверку, жив ли монстр, если монстр мертв, его нужно удалить из массива с помощью одной из функций
# if not encountered_mob.alive
# player_weapon = Axe("N-word crusher")
# player_weapon2 = Sword("Faggot slayer")
# healing_potion = Potion("Baltica 9")
# healing_potion2 = AdvancedPotion("Okhota Krepkaya")
