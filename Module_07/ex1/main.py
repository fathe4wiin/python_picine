from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck

def main():
    print("=== DataDeck Deck Builder ===")
    print("Building deck with different card types...")
    
    deck = Deck()
    
    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))
    deck.add_card(SpellCard("Lightning Bolt", 3, "Common", "damage"))
    deck.add_card(ArtifactCard("Mana Crystal", 2, "Rare", 3, "+1 mana per turn"))
    
    print(f"Deck stats: {deck.get_deck_stats()}")
    
    print("\nDrawing and playing cards:")
    
    deck.shuffle()
    try:
        while True:
            card = deck.draw_card()
            type_label = card.__class__.__name__.replace("Card", "")
            print(f"Drew: {card.name} ({type_label})")
            
            play_result = card.play({})
            print(f"Play result: {play_result}")
    except IndexError:
        pass

    print("\nPolymorphism in action: Same interface, different card behaviors!")

if __name__ == "__main__":
    main()