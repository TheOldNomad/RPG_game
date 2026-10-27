from __future__ import annotations

from typing import TYPE_CHECKING

from player_subsystems_and_data.player_skill_system.character_perks import perk_menu_and_list_mediator
from player_subsystems_and_data.player_skill_system.character_perks.perk_list import PerkList


def acquire_perk(perk_list: PerkList) -> None:
    perk_menu_and_list_mediator.view_all_perks(perk_list)
    perk_index = input("Please, choose the perk you would like to acquire")
