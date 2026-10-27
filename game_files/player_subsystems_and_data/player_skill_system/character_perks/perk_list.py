from player_subsystems_and_data.player_skill_system.character_perks import perk_module
from player_subsystems_and_data.player_skill_system.character_perks.perk import Perk

from game_files.entities.player import Player


class PerkList:
    def __init__(self) -> None:
        self.perk_list = []

    def view_perk_list(self) -> None:
        print(f"{self.perk_list}")

    def choose_skill(self, perk_index: int) -> Perk:
        return self.perk_list[perk_index]

    def acquire_skill(self, player: Player, perk_index: int) -> None:
        player.chosen_perk = self.perk_list[perk_index]
