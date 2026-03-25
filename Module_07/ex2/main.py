from ex2.EliteCard import EliteCard

def main():
    print("=== DataDeck Ability System ===")
    
    # Initialize an EliteCard (Name, Cost, Rarity, Attack, Health, Mana)
    # Based on the Expected Output Example
    warrior = EliteCard("Arcane Warrior", 6, "Legendary", 5, 10, 7)

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print(f"\nPlaying {warrior.name} (Elite Card):")
    print(warrior.play({}))

    print("\nCombat phase:")
    # Test Combatable: attack
    attack_result = warrior.attack("Enemy")
    print(f"Attack result: {attack_result}")

    # Test Combatable: defend
    # We simulate incoming damage of 5. With 3 blocked (as in our logic), 
    # damage taken should be 2.
    defense_result = warrior.defend(5)
    print(f"Defense result: {defense_result}")

    print("\nMagic phase:")
    # Test Magical: cast_spell
    spell_result = warrior.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print(f"Spell cast: {spell_result}")

    # Test Magical: channel_mana
    # If starting at 7 mana, using 4 for spell = 3. Channeling 3 = 6.
    # Note: Adjust values to match your specific balance or the PDF example.
    mana_result = warrior.channel_mana(3)
    print(f"Mana channel: {mana_result}")

    print("\nMultiple interface implementation successful!")

if __name__ == "__main__":
    main()