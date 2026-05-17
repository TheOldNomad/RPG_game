from game_files.entities.player import Player


class AttackMenu:
    def choose_target_to_attack(self, monster_list: list, player_character: Player) -> None:
        user_input = input("You see monsters, which one do you want to attack? Use the numpad to choose the monster")
        current_monster_index = int(user_input)
        if not user_input.isdigit():
            print("This option is not supported. Use an integer to choose a command")
            return
        if current_monster_index < 0 or current_monster_index >= len(monster_list):
            print("This monster has already perished. Would you like to attack the other one?")
            return
        player_character.deal_damage(monster_list[current_monster_index])
        if not monster_list[current_monster_index].alive:
            monster_list.pop(current_monster_index)
