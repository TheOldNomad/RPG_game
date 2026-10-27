from abc import ABC, abstractmethod


class CharacterSheet(ABC):
    @abstractmethod
    def see_player_attributes(self) -> None:
        pass

    @abstractmethod
    def change_attributes(self, points_to_add: int, stat_to_change: str) -> None:
        pass


class PlayerBaseAttributes(CharacterSheet):
    def __init__(self) -> None:
        self.strength = 0
        self.magic = 0
        self.endurance = 0
        self.intelligence = 0
        self.perception = 0
        self.dexterity = 0

    def see_player_attributes(self) -> None:
        print(f"""{self.strength}\n
            f"{self.magic}\n
            f"{self.endurance}\n
            f"{self.intelligence}\n
            f"{self.perception}\n
            f"{self.dexterity}\n""")

    def change_attributes(self, points_to_add: int, stat_to_change: str) -> None:
        match stat_to_change:
            case "strength":
                self.strength += points_to_add
            case "magic":
                self.magic += points_to_add
            case "endurance":
                self.endurance += points_to_add
            case "intelligence":
                self.intelligence += points_to_add
            case "perception":
                self.perception += points_to_add
            case "dexterity":
                self.dexterity += points_to_add
            case _:
                print("No such attribute, try again")
                return
