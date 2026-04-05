from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy, InvalidStrategyError

def run_tournament(name, opponents):
    print(f"Tournament {name}")
    print(f"*** Tournament ***\n{len(opponents)} opponents involved")
    
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            f1, s1 = opponents[i]
            f2, s2 = opponents[j]
            c1 = f1.create_base()
            c2 = f2.create_base()
            
            print("* Battle *")
            print(f"{c1.describe()}\nvs.\n{c2.describe()}\nnow fight!")
            
            try:
                s1.act(c1)
                s2.act(c2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return

if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()
    heal = HealingCreatureFactory()
    trans = TransformCreatureFactory()
    
    norm = NormalStrategy()
    agg = AggressiveStrategy()
    defen = DefensiveStrategy()

    run_tournament("0 (basic)", [(flame, norm), (heal, defen)])
    run_tournament("1 (error)", [(flame, agg), (heal, defen)])
    run_tournament("2 (multiple)", [(aqua, norm), (heal, defen), (trans, agg)])