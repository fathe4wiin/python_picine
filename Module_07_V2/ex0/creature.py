from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, element_type: str):
        self.name = name
        self.element_type = element_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.element_type} type Creature"


class Flameling(Creature):
    def __init__(self, name: str, element_type: str):
        super().__init__(name, element_type)

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self, name: str, element_type: str):
        super().__init__(name, element_type)

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self, name: str, element_type: str):
        super().__init__(name, element_type)

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    def __init__(self, name: str, element_type: str):
        super().__init__(name, element_type)

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"
