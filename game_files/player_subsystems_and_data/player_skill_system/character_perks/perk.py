from abc import ABC, abstractmethod


class Perk:
    description: str
    name: str

    def __init__(self, name: str, description: str, effect: int) -> None:
        self.name = name
        self.description = description
        self.effect = effect

    def view_perk_description(self) -> str:
        return self.description
