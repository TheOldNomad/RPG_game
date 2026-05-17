from game_files.entities.monster import Monster
from game_files.entities.player import Player
from game_files.menus.players_action_menu import PlayersActionMenu

if __name__ == "__main__":
    encountered_mob = Monster("stalnoye dildo Damirchika")
    encountered_mob2 = Monster("popka Nekrasova")
    monster_list = [encountered_mob, encountered_mob2]
    active_player = Player("Bimba", "shalunishka")
    introductory_interface = PlayersActionMenu()
    while active_player.alive:
        introductory_interface.introductory_choice(monster_list, active_player)
        if active_player.health_points <= 50:
            user_input = input("Your health seems low. Would you like to drink a potion?")
            if user_input == "Yes":
                active_player.healing(active_player)
            else:
                pass
        for current_monster in monster_list:
            current_monster.deal_damage(active_player)
        if not encountered_mob.alive and not encountered_mob2.alive:
            print("You have successfully cleared out a dungeon! Now go and get yourself a job, you nerd")
            break
