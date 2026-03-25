from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable

class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, attack_val: int, health: int, card_id: str):
        super().__init__(name, cost, rarity)
        self.attack_val = attack_val
        self.health = health
        self.card_id = card_id
        self.wins = 0
        self.losses = 0
        self.rating = 1200

    def play(self, game_state: dict) -> dict:
        return {'card_played': self.name, 'type': 'Tournament'}

    def attack(self, target) -> dict:
        return {'attacker': self.name, 'damage': self.attack_val}

    def defend(self, incoming_damage: int) -> dict:
        self.health -= incoming_damage
        return {'defender': self.name, 'still_alive': self.health > 0}

    def get_combat_stats(self) -> dict:
        return {'attack': self.attack_val, 'health': self.health}

    def calculate_rating(self) -> int:
        return self.rating + (self.wins * 20) - (self.losses * 10)

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += (wins * 16)

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= (losses * 16)

    def get_rank_info(self) -> dict:
        return {'rating': self.rating, 'record': f"{self.wins}-{self.losses}"}

    def get_tournament_stats(self) -> dict:
        return {
            'card_id': self.card_id,
            'name': self.name,
            'rating': self.rating,
            'record': f"{self.wins}-{self.losses}"
        }