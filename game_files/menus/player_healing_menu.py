from from game_files.entities.player import Player

class PlayerHealingMenu:
    def take_health_potion(self, player_character: Player) -> None:
        user_input = input("Your health seems low. Would you like to drink a potion?
        1 - "Yes"
        2 - "No")
        if user_input not in {"1", "2"}:
            print("No such option, use your numpad, genius")
            return
        elif user_input == "Yes":
            player_character.healing(player_character)
        else:
            return