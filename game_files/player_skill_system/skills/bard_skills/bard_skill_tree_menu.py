from game_files.player_classes.bard_class import BardPlayer


def pick_new_skill(bard_character: BardPlayer) -> None:
    bard_character.skill_tree.view_relevant_skill_tree()
    skill_to_pick = int(input("Please, pick the skill you like"))
    current_skill = bard_character.skill_tree.choose_skill(skill_to_pick)
    if not skill_to_pick:
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
        current_skill.view_skill_description()
        return
    if player_command == "2":
        bard_character.skill_tree.acquire_skill(bard_character, skill_to_pick)
    else:
        return
