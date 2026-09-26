from game_files.entities.player import Player
from game_files.player_classes.bard_class import BardPlayer
from game_files.player_classes.cleric_class import ClericPlayer
from game_files.player_classes.mage_class import MagePlayer
from game_files.player_classes.thief_class import ThiefPlayer
from game_files.player_classes.warrior_class import WarriorPlayer


def match_character_class(new_player: BardPlayer | ClericPlayer | MagePlayer | ThiefPlayer | WarriorPlayer) -> None:
    match new_player:
        case WarriorPlayer():
            new_player.warrior_skill_tree_menu.pick_new_skill()
        case MagePlayer():
            new_player.mage_skill_tree_menu.pick_new_skill()
        case ThiefPlayer():
            new_player.thief_skill_tree_menu.pick_new_skill()
        case BardPlayer():
            new_player.bard_skill_tree_menu.pick_new_skill()
        case ClericPlayer():
            new_player.cleric_skill_tree_menu.pick_new_skill()
        case _:
            raise ValueError(f"Unknown character class: {type(new_player)}")
