from game_files.entities.player import Player
from game_files.healing_mechanic.healing_mediator import HealingMediator


class PlayerHealingMenu:
    def take_health_potion(self, player_character: Player) -> None:
        healing_mediator = HealingMediator()
        user_input = input("Your health seems low. Would you like to drink a potion?1 - Yes2 - No")
        if user_input not in {"1", "2"}:
            print("No such option, use your numpad, genius")
            return
        if user_input == "Yes":
            healing_mediator.use_health_potion(player_character)
        else:
            return
