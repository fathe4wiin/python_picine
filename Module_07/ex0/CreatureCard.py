try:
    from .Card import Card
except ImportError:
    from Card import Card

class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        if attack < 0 or health < 0:
            raise ValueError("Attack and health must be non-negative integers.")
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        return {
        'card_played': self.name,
        'mana_used': self.cost,
        'effect': 'Creature summoned to battlefield'
    }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({
            "attack": self.attack,
            "health": self.health
        })
        return info

    def is_playable(self, available_mana: int) -> bool:
        return super().is_playable(available_mana)
    
    def attack_target(self, target) -> dict:
        return {
        'attacker': self.name,
        'target': str(target),
        'damage_dealt': self.attack,
        'combat_resolved': True
    }