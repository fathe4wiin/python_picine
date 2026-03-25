from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy

class GameEngine:
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns = 0

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        self.turns += 1
        hand = [
            self.factory.create_creature(),
            self.factory.create_creature("Goblin"),
            self.factory.create_spell()
        ]
        execution = self.strategy.execute_turn(hand, [])
        return {
            'turns_simulated': self.turns,
            'strategy_used': self.strategy.get_strategy_name(),
            'total_damage': execution['damage_dealt'],
            'cards_created': len(hand)
        }

    def get_engine_status(self) -> dict:
        return {'status': 'active', 'factory': type(self.factory).__name__}