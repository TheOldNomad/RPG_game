from game_files.monster import Monster
from game_files.player_character import Player

if __name__ == "__main__":
    encountered_mob = Monster("stalnoye dildo Damirchika")
    encountered_mob2 = Monster("popka Nekrasova")
    encountered_mobs = [encountered_mob, encountered_mob2]
    active_player = Player("Bimba", "shalunishka")
    while active_player.alive:
        active_player.choosing_target_to_attack(encountered_mobs)
        if active_player.health_points <= 50:
            user_input = input("Your health seems low. Would you like to drink a potion?")
            if user_input == "Yes":
                active_player.healing(active_player)
            else:
                pass
        for current_monster in encountered_mobs:
            current_monster.dealing_damage(active_player)
        if not encountered_mob.alive and not encountered_mob2.alive:
            print("You have successfully cleared out a dungeon! Now go and get yourself a job, you nerd")
            break


# немного перестроить структуру: добавить для пользователя меню с выбором, что он хочет делать: атаковать монстра, открыть
# инвентарь, пройти в другую локацию, и т.д. При выборе соответствующей опции открывается другой цикл, который отвечает за
# соответствующую операцию, который при этом расположен в соответствующем файле. Таким образом, главный файл будет отсылать
# к другим файлам

# настроить параметризацию строчек в питоне (чтобы при запуске стринга выводилось имя конкретного монстра, в том числе)
