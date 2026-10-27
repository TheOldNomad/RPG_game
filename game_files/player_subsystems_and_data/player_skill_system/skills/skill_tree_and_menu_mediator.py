from game_files.entities.player import Player
from game_files.player_subsystems_and_data.player_skill_system.skills.skill import Skill


def view_relevant_skill_tree(player_character: Player) -> None:
    player_character.skill_tree.view_character_skill_tree()


def select_skill(player_character: Player, skill_index: int) -> None:
    current_skill = player_character.skill_tree.choose_skill(skill_index)
    if not current_skill:
        print("No such skill, try again")
        return


def view_selected_skill_description(current_skill: Skill) -> str:
    return current_skill.view_skill_description()


def acquire_selected_skill(player_character: Player, skill_index: int) -> None:
    player_character.skill_tree.acquire_skill(player_character, skill_index)
