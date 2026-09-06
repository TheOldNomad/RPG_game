from abc import ABC, abstractmethod


class Skill(ABC):
    required_level: int
    description: str
    name: str

    @abstractmethod
    def view_skill_description(self) -> str:
        pass


class StatChangeSkill(Skill):
    def __init__(self, name: str, description: str, effect: int) -> None:
        self.name = name
        self.description = description
        self.effect = effect

    def view_skill_description(self) -> str:
        return self.description


class AbilityChangeSkill(Skill):
    def __init__(self, name: str, description: str, effect: int) -> None:
        self.name = name
        self.description = description
        self.effect = effect

    def view_skill_description(self) -> str:
        return self.description
