from game_files.entities.monster import Monster
from game_files.entities.player import Player
from game_files.menus.players_action_menu import PlayersActionMenu
from game_files.menus.player_healing_menu import PlayerHealingMenu
from game_files.menus.monster_attack_menu import MonsterAttackMenu

if __name__ == "__main__":
    encountered_mob = Monster("stalnoye dildo Damirchika")
    encountered_mob2 = Monster("popka Nekrasova")
    monster_list = [encountered_mob, encountered_mob2]
    active_player = Player("Bimba", "shalunishka")
    introductory_interface = PlayersActionMenu()
    healing_interface = PlayerHealingMenu()
    monster_attack_mechanic = MonsterAttackMenu()
    while active_player.alive:
        introductory_interface.introductory_choice(monster_list, active_player)
        if active_player.health_points <= 50:
            healing_interface.take_health_potion(active_player)
        for current_monster in monster_list:
            monster_attack_mechanic.register_monster_damage(active_player, current_monster)
        if not encountered_mob.alive and not encountered_mob2.alive:
            print("You have successfully cleared out a dungeon! Now go and get yourself a job, you nerd")
            break
