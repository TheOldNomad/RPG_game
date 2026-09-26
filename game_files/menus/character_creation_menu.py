from game_files.player_classes.bard_class import BardPlayer
from game_files.player_classes.cleric_class import ClericPlayer
from game_files.player_classes.mage_class import MagePlayer
from game_files.player_classes.thief_class import ThiefPlayer
from game_files.player_classes.warrior_class import WarriorPlayer
from game_files.player_skill_system.character_perks import perk_menu
from game_files.player_skill_system.skills import character_skill_set_mediator


def create_new_character() -> None:
    character_name = input("Please, choose the name of your character")
    character_class = input("""Please, choose the class of your character:\n
    1 - Warrior\n
    2 - Mage\n
    3 - Thief\n
    4 - Bard\n
    5 - Cleric""")
    match character_class:
        case "1":
            new_player = WarriorPlayer(character_name)
        case "2":
            new_player = MagePlayer(character_name)
        case "3":
            new_player = ThiefPlayer(character_name)
        case "4":
            new_player = BardPlayer(character_name)
        case "5":
            new_player = ClericPlayer(character_name)
        case _:
            print("No such option, try again")
            return
    character_skill_set_mediator.match_character_class(new_player)
    perk_menu.acquire_perk()
