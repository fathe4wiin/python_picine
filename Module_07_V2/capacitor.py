from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing():
    print("Testing Creature with healing capability")
    factory = HealingCreatureFactory()
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())

    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_transform():
    print("\nTesting Creature with transform capability")
    factory = TransformCreatureFactory()
    base = factory.create_base()

    print("base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())


if __name__ == "__main__":
    test_healing()
    test_transform()
