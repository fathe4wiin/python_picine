from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform

def main():
    print("=== DataDeck Tournament Platform ===")
    platform = TournamentPlatform()
    
    c1 = TournamentCard("Fire Dragon", 5, "Legendary", 8, 10, "dragon_001")
    c2 = TournamentCard("Ice Wizard", 4, "Rare", 6, 8, "wizard_001")
    
    for c in [c1, c2]:
        platform.register_card(c)
        print(f"{c.name} (ID: {c.card_id}):")
        print(f"- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {c.rating}")
        print(f"- Record: {c.wins}-{c.losses}")

    print("\nCreating tournament match...")
    match = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {match}")

    print("\nTournament Leaderboard:")
    for i, entry in enumerate(platform.get_leaderboard(), 1):
        print(f"{i}. {entry}")

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())
    print("\n=== Tournament Platform Successfully Deployed! ===")

if __name__ == "__main__":
    main()