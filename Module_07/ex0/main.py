try:
    from . import CreatureCard
except ImportError:
    from CreatureCard import CreatureCard

def main():
    print("=== DataDeck Card Foundation ===")
    print("Testing Abstract Base Class Design:")
    
    # 1. Create the instance
    # Requirement: name, cost, rarity, attack, health 
    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    goblin = CreatureCard("Goblin Warrior", 2, "Common", 2, 2)

    # 2. Test get_card_info() [cite: 201, 203]
    print("CreatureCard Info:")
    print(dragon.get_card_info())

    # 3. Test playing the card with sufficient mana 
    available_mana = 6
    print(f"\nPlaying {dragon.name} with {available_mana} mana available:")
    
    # Check is_playable 
    playable = dragon.is_playable(available_mana)
    print(f"Playable: {playable}")
    
    if playable:
        # play() returns the result dict 
        play_result = dragon.play({"current_mana": available_mana})
        print(f"Play result: {play_result}")

    # 4. Test attack_target() [cite: 201, 203]
    print(f"\n{dragon.name} attacks {goblin.name}:")
    attack_result = dragon.attack_target(goblin)
    print(f"Attack result: {attack_result}")

    # 5. Test insufficient mana 
    low_mana = 3
    print(f"\nTesting insufficient mana ({low_mana} available):")
    print(f"Playable: {dragon.is_playable(low_mana)}")
    
    print("\nAbstract pattern successfully demonstrated!")

if __name__ == "__main__":
    main()