from game_files.player_skill_system.skills.character_skill_set_mediator import character_skill_set_mediator

def create_new_character() -> None:
    character_name = input("Please, choose the name of your character")
    character_class = input("""Please, choose the class of your character:\n
    1 - Warrior\n
    2 - Mage\n
    3 - Thief\n
    4 - Bard\n
    5 - Cleric""")
    character_skill_set_mediator.match_character_class(character_class)

