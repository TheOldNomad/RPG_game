from abc import ABC, abstractmethod


class Skill(ABC):
    required_level: int

    @abstractmethod
    def view_skill_description(self) -> str:
        pass
