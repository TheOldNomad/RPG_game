from abc import ABC, abstractmethod


class Perk:
    description: str
    name: str

    def __init__(self) -> None:
        self.name = name
        self.description = description
        self.effect = effect

    def view_perk_description(self) -> str:
        return self.description
    

