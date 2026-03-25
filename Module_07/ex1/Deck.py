import random
from ex0.Card import Card

class Deck:
    def __init__(self):
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for i, card in enumerate(self.cards):
            if card.name == card_name:
                self.cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise IndexError("Cannot draw from an empty deck")
        return self.cards.pop()

    def get_deck_stats(self) -> dict:
        from ex0.CreatureCard import CreatureCard
        from ex1.SpellCard import SpellCard
        from ex1.ArtifactCard import ArtifactCard

        stats = {
            'total_cards': len(self.cards),
            'creatures': 0,
            'spells': 0,
            'artifacts': 0,
            'avg_cost': 0.0
        }
        
        if not self.cards:
            return stats

        total_cost = 0
        for card in self.cards:
            total_cost += card.cost
            if isinstance(card, CreatureCard):
                stats['creatures'] += 1
            elif isinstance(card, SpellCard):
                stats['spells'] += 1
            elif isinstance(card, ArtifactCard):
                stats['artifacts'] += 1
        
        stats['avg_cost'] = total_cost / len(self.cards)
        return stats