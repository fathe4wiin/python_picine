from abc import ABC, abstractmethod
from typing import Optional


class Creature(ABC):
    def __init__(self, name: str, element_type: str):
        self.name = name
        self.element_type = element_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.element_type} type Creature"


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: Optional[str] = None) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self):
        self.is_transformed = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str, element_type: str):
        Creature.__init__(self, name, element_type)

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self, target: Optional[str] = None) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str, element_type: str):
        Creature.__init__(self, name, element_type)

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self, target: Optional[str] = None) -> str:
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, element_type: str):
        Creature.__init__(self, name, element_type)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.is_transformed = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, element_type: str):
        Creature.__init__(self, name, element_type)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.is_transformed = False
        return f"{self.name} stabilizes its form."
