from game_files.player_classes.warrior_class import WarriorPlayer


def pick_new_skill(warrior_character: WarriorPlayer):
    warrior_character.skill_tree.view_relevant_skill_tree()
    