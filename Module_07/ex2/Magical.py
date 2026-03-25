from abc import ABC, abstractmethod

class Magical(ABC):
    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Abstract method for executing a spell."""
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """Abstract method for managing or recovering mana."""
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """Abstract method to retrieve mana-related information."""
        pass