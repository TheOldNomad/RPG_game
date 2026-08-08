class CharacterCreationMenu:
    def create_new_character(self) -> None:
        character_name = input("Please, choose the name of your character")
        character_class = input("""Please, choose the class of your character:\n
        1 - Warrior\n
        2 - Mage\n
        3 - Thief\n
        4 - Bard\n
        5 - Cleric""")
