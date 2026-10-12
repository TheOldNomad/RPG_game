from game_files.entities.player import Player
from game_files.player_skill_system.character_perks import perk_module
from game_files.player_skill_system.character_perks.perk import Perk


class PerkList:
    def __init__(self) -> None:
        self.perk_list = []

    def view_perk_list(self) -> None:
        print(f"{self.perk_list}")

    def choose_skill(self, perk_index: int) -> Perk:
        return self.perk_list[perk_index]

    def acquire_skill(self, player: Player, perk_index: int) -> None:
        player.chosen_perk = self.perk_list[perk_index]
