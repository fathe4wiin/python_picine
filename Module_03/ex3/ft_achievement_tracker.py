def main():
    print("=== Achievement Tracker System ===")

    alice_achievements = {
        'First Blood',
        'Unstoppable',
        'Baron Slayer',
        'Visionary'}
    bob_achievements = {
        'First Blood',
        'Dragon Slayer',
        'Pentakill',
        'Visionary'}
    charlie_achievements = {
        'Dragon Slayer',
        'Unstoppable',
        'Baron Slayer',
        'Sharpshooter',
        'Visionary'}

    fathe4wiin_achievements = {
        'First Blood',
        'Dragon Slayer',
        'Unstoppable',
        'Baron Slayer',
        'Pentakill',
        'Sharpshooter',
        'Visionary',
        'Legendary',
        'Ultimate Master'}

    print(f"Player alice achievements: {alice_achievements}")
    print(f"Player bob achievements: {bob_achievements}")
    print(f"Player charlie achievements: {charlie_achievements}")
    print(f"Player fathe4wiin achievements: {fathe4wiin_achievements}")

    print("\n=== Achievement Analytics ===")

    all_achievements = (
        alice_achievements |
        bob_achievements |
        charlie_achievements |
        fathe4wiin_achievements
    )
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")

    common_to_all = (
        alice_achievements &
        bob_achievements &
        charlie_achievements &
        fathe4wiin_achievements
    )
    print(f"Common to all players: {common_to_all}")

    players = [
        alice_achievements,
        bob_achievements,
        charlie_achievements,
        fathe4wiin_achievements]
    rare = set()

    for achievement in all_achievements:
        count = 0
        for player in players:
            if achievement in player:
                count += 1
        if count == 1:
            rare.add(achievement)

    print(f"Rare achievements: {rare}")

    alice_vs_bob_common = alice_achievements & bob_achievements
    print(f"Alice vs Bob common: {alice_vs_bob_common}")

    alice_unique = alice_achievements - bob_achievements
    print()
    print(f"Alice unique: {alice_unique}")

    bob_unique = bob_achievements - alice_achievements
    print(f"Bob unique: {bob_unique}")

    fathe4wiin_unique = fathe4wiin_achievements - \
        (alice_achievements | bob_achievements | charlie_achievements)
    print(f"fathe4wiin unique: {fathe4wiin_unique}")


if __name__ == "__main__":
    main()
