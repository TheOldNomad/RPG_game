import array
import random

from .character import Player
from .player_character_inventory import AdvancedPotion, Axe, Potion, Sword, inventory_navigation


class Player(Player):
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
        self.active_inventory = []
        player_weapon = Axe("N-word crusher")
        player_weapon2 = Sword("Faggot slayer")
        healing_potion = Potion("Baltica 9")
        healing_potion2 = AdvancedPotion("Okhota Krepkaya")

    def choosing_target_to_attack(self, encountered_mobs: array) -> None:
        user_input = input("You see monsters, which one do you want to attack? Use the numpad to choose the monster")
        current_monster_index = int(user_input)
        if not user_input.isdigit():
            print("This option is not supported. Use an integer to choose a command")
            return
        if current_monster_index < 0 or current_monster_index >= len(encountered_mobs):
            print("This monster has already perished. Would you like to attack the other one?")
            return
        self.dealing_damage(encountered_mobs[current_monster_index])
        if not encountered_mobs[current_monster_index].alive:
            encountered_mobs.pop(current_monster_index)

    def introductory_choice(self, encountered_mobs: array) -> None:
        player_choice = input("""You see a suspiciously looking cave. What will be your actions?" \
        "1 - open the inventory" \
        "2 - enter the cave""")
        if player_choice not in {"1", "2"}:
            print("No such option exists, try again, smartass")
        elif player_choice == "1":
            inventory_navigation()
        else:
            self.choosing_target_to_attack(encountered_mobs)


# Вставить сюда проверку, жив ли монстр, если монстр мертв, его нужно удалить из массива с помощью одной из функций
# if not encountered_mob.alive
