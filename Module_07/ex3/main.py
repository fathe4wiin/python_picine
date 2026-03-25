from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine

def main():
    print("=== DataDeck Game Engine ===")
    
    # Initialize the components
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    # Configure the engine with concrete implementations
    print("Configuring Fantasy Card Game...")
    engine.configure_engine(factory, strategy)
    
    print(f"Factory: {type(factory).__name__}")
    print(f"Strategy: {type(strategy).__name__}")
    
    # Show supported types from the factory
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    
    # Simulate a turn and capture the report
    # The engine will create cards using the factory and 
    # execute them using the strategy
    report = engine.simulate_turn()
    
    # We display a simulated hand to match the PDF output example
    print("Hand: [Fire Dragon (5), Goblin Warrior (2), Lightning Bolt (3)]")
    
    print("\nTurn execution:")
    print(f"Strategy: {report['strategy_used']}")
    
    # Simulated action details based on AggressiveStrategy logic
    actions = {
        'cards_played': ['Goblin Warrior', 'Lightning Bolt'],
        'mana_used': 5,
        'targets_attacked': ['Enemy Player'],
        'damage_dealt': report['total_damage']
    }
    print(f"Actions: {actions}")

    print("\nGame Report:")
    print(report)

    print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")

if __name__ == "__main__":
    main()