from abc import ABC, abstractmethod


class Perk(ABC):
    @abstractmethod
    def view_perk_description(self) -> str:
        pass
