
class Plant:
    """
    A class to represent a plant.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a new Plant instance.
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def creation_info(self) -> None:
        """
        Print creation info for the plant.
        """
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def main() -> None:
    """
    Main function to produce plants from a factory list.
    """
    plant_data: list[tuple[str, int, int]] = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]

    plants: list[Plant] = []

    for name, height, age in plant_data:
        plant = Plant(name, height, age)
        plants.append(plant)

    print("=== Plant Factory Output ===")
    for plant in plants:
        plant.creation_info()
    print(f"Total plants created: {len(plants)}")


if __name__ == "__main__":
    main()
