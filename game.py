from game_files.entities.monster import Monster
from game_files.entities.player import Player
from game_files.modules.mediator_and_menu_module import players_action_menu, player_healing_menu, monster_attack_menu

if __name__ == "__main__":
    encountered_mob = Monster("stalnoye dildo Damirchika")
    encountered_mob2 = Monster("popka Nekrasova")
    monster_list = [encountered_mob, encountered_mob2]
    active_player = Player("Bimba", "shalunishka")
    while active_player.alive:
        players_action_menu.introductory_choice(monster_list, active_player)
        if active_player.health_points <= 50:
            player_healing_menu.take_health_potion(active_player)
        for current_monster in monster_list:
            monster_attack_menu.register_monster_damage(active_player, current_monster)
        if not encountered_mob.alive and not encountered_mob2.alive:
            print("You have successfully cleared out a dungeon! Now go and get yourself a job, you nerd")
            break
