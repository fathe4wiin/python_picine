from ex3.GameStrategy import GameStrategy

class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        played = []
        mana_spent = 0
        for card in sorted(hand, key=lambda x: x.cost):
            played.append(card.name)
            mana_spent += card.cost
            
        return {
            'cards_played': played,
            'mana_used': mana_spent,
            'targets_attacked': ['Enemy Player'],
            'damage_dealt': 8
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return sorted(available_targets, reverse=True)