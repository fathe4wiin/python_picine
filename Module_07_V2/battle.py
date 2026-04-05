from ex0 import FlameFactory, AquaFactory

def verify_factory(factory):
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())

def fight(f1, f2):
    print("Testing battle")
    c1 = f1.create_base()
    c2 = f2.create_base()
    
    print(f"{c1.describe()}\n VS.\n{c2.describe()}")
    print("fight!")
    print(c1.attack())
    print(c2.attack())

if __name__ == "__main__":
    flame_f = FlameFactory()
    aqua_f = AquaFactory()
    
    verify_factory(flame_f)
    verify_factory(aqua_f)
    fight(flame_f, aqua_f)