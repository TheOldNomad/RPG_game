from game_files.player_skill_system.skills.bard_skill_tree_menu import bard_skill_tree_menu
from game_files.player_skill_system.skills.cleric_skill_tree_menu import cleric_skill_tree_menu
from game_files.player_skill_system.skills.mage_skill_tree_menu import mage_skill_tree_menu
from game_files.player_skill_system.skills.thief_skill_tree_menu import thief_skill_tree_menu
from game_files.player_skill_system.skills.warrior_skill_tree_menu import warrior_skill_tree_menu


def match_character_class(character_class: str) -> None:
    match character_class:
        case "1":
            warrior_skill_tree_menu.pick_new_skill()
        case "2":
            mage_skill_tree_menu.pick_new_skill()
        case "3":
            thief_skill_tree_menu.pick_new_skill()
        case "4":
            bard_skill_tree_menu.pick_new_skill()
        case "5":
            cleric_skill_tree_menu.pick_new_skill()
