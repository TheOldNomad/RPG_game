from __future__ import annotations

from typing import TYPE_CHECKING

from game_files.player_skill_system.skills import skill_tree_and_menu_mediator

if TYPE_CHECKING:
    from game_files.entities.player import Player


def pick_new_skill(player_character: Player) -> None:
    skill_tree_and_menu_mediator.view_relevant_skill_tree(player_character)
    skill_to_pick = int(input("Please, pick the skill you like"))
    current_skill = skill_tree_and_menu_mediator.select_skill(player_character, skill_to_pick)
    if not current_skill:
        print("No such skill, try again")
        return
    player_command = input(f"""You chose {current_skill}. What will be your actions?\n
                           1 - view skill description\n
                           2 - acquire skill\n
                           3 - go back\n""")
    if player_command not in {"1", "2", "3"}:
        print("No such command, try again")
        return
    if player_command == "1":
        skill_tree_and_menu_mediator.view_selected_skill_description(current_skill)
        return
    if player_command == "2":
        skill_tree_and_menu_mediator.acquire_selected_skill(player_character, skill_to_pick)
    else:
        return
