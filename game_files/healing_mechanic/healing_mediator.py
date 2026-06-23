from game_files.entities.player import Player
from game_files.items.potions import HealthPotion


class HealingMediator:
    def calculate_health_points_to_regenerate(self, player_character: Player, potion_to_use: HealthPotion) -> None:
        hp_to_regenerate = player_character.inventory.get_health_potion_parameters(potion_to_use)
        player_character.healing(player_character, hp_to_regenerate)

    def use_health_potion(self, player_character: Player, potion_to_use: HealthPotion, potion_to_use_index: int) -> None:
        self.calculate_health_points_to_regenerate(player_character)
        player_character.inventory.discard_item(potion_to_use_index)
