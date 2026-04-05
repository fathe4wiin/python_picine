from abc import ABC, abstractmethod
from .creature import Creature, Sproutling, Bloomelle, Shiftling, Morphagon

class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass

class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling("Sproutling", "Grass")

    def create_evolved(self) -> Bloomelle:
        return Bloomelle("Bloomelle", "Grass/Fairy")

class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling("Shiftling", "Normal")

    def create_evolved(self) -> Morphagon:
        return Morphagon("Morphagon", "Normal/Dragon")