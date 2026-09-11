from game_files.player_classes.bard_class import BardPlayer
from game_files.player_classes.cleric_class import ClericPlayer
from game_files.player_classes.mage_class import MagePlayer
from game_files.player_classes.thief_class import ThiefPlayer
from game_files.player_classes.warrior_class import WarriorPlayer
from game_files.player_skill_system.skills.bard_skills import bard_skill_tree_menu
from game_files.player_skill_system.skills.cleric_skills import cleric_skill_tree_menu
from game_files.player_skill_system.skills.mage_skills import mage_skill_tree_menu
from game_files.player_skill_system.skills.thief_skills import thief_skill_tree_menu
from game_files.player_skill_system.skills.warrior_skills import warrior_skill_tree_menu


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
