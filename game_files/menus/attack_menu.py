from game_files.entities.player import Player
from game_files.attack_mechanic.attack_mediator import AttackMediator

class AttackMenu:
    def choose_target_to_attack(self, monster_list: list, player_character: Player) -> None:
        attack_mediator = AttackMediator()
        user_input = input("You see monsters, what are your actions? 1 - attack one of the monsters 2 - run away")
        if user_input not in {"1", "2"}:
            print("Wrong option, imbecile, try again")
        elif user_input == "2":
            print("No way to run, baby!")
            return
        else:
            monster_to_attack = input("which one do you want to attack? Use the numpad to choose the monster")
            current_monster_index = int(monster_to_attack)
            if not monster_to_attack.isdigit():
                print("This option is not supported. Use an integer to choose a command")
                return
            if current_monster_index < 0 or current_monster_index >= len(monster_list):
                print("This monster has already perished. Would you like to attack the other one?")
                return
            attack_mediator.compute_player_dealt_damage_to_mob(player_character, monster_list, current_monster_index, item_to_get_parameters_from)