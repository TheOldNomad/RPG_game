from game_files.entities.player import Player


class HealingMediator:
    def calculate_health_points_to_regenerate(self, player_character: Player) -> None:
        hp_to_regenerate = player_character.inventory.get_health_potion_parameters()
        player_character.healing(player_character, hp_to_regenerate)

    def use_health_potion(self, player_character: Player) -> None:
        self.calculate_health_points_to_regenerate(player_character)
