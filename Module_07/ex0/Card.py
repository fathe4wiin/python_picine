from abc import ABC, abstractmethod

class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    def play(self, game_state: dict) -> dict:
        """Default: Returns unchanged game state. Subclasses override for specific card effects."""
        return game_state
    
    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }
    
    def is_playable(self, available_mana: int) -> bool:
        """Default: Card is playable if available mana is sufficient. Subclasses can add more conditions."""
        return available_mana >= self.cost
    
    