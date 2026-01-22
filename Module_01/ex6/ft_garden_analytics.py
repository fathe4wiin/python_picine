
class Plant:
    """Base class for plants."""

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def grow(self, amount: int = 1) -> None:
        """Simulate growth by increasing height."""
        self.height += amount

    def get_info(self) -> str:
        """Return formatted plant info."""
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """Flowering plant that can bloom."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.is_blooming: bool = False

    def bloom(self) -> None:
        """Set flowering status to true."""
        self.is_blooming = True

    def get_info(self) -> str:
        """Return formatted info including flowering status."""
        status = "blooming" if self.is_blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers ({status})"


class PrizeFlower(FloweringPlant):
    """Prize-winning flower with points."""

    def __init__(
        self, name: str, height: int, age: int, color: str, prize_points: int
    ) -> None:
        super().__init__(name, height, age, color)
        self.prize_points: int = prize_points

    def get_info(self) -> str:
        """Return formatted info including prize points."""
        base_info = super().get_info()
        return f"{base_info}, Prize points: {self.prize_points}"


class GardenManager:
    """Manages a garden and its statistics."""

    class GardenStats:
        """Internal class to track garden statistics."""

        def __init__(self) -> None:
            self.plants_added: int = 0
            self.total_growth: int = 0
            self.regular_count: int = 0
            self.flowering_count: int = 0
            self.prize_count: int = 0

        def add_plant(self, plant: "Plant") -> None:
            """Update stats when a plant is added."""
            self.plants_added += 1
            if isinstance(plant, PrizeFlower):
                self.prize_count += 1
            elif isinstance(plant, FloweringPlant):
                self.flowering_count += 1
            else:
                self.regular_count += 1

        def record_growth(self, amount: int) -> None:
            """Update total growth stats."""
            self.total_growth += amount

        def get_report(self) -> str:
            """Generate a stats report string."""
            return (
                f"Plants added: {self.plants_added}, "
                f"Total growth: {self.total_growth}cm\n"
                f"Plant types: {self.regular_count} regular, "
                f"{self.flowering_count} flowering, "
                f"{self.prize_count} prize flowers"
            )

    _gardens: dict[str, "GardenManager"] = {}

    def __init__(self, owner_name: str) -> None:
        self.owner_name: str = owner_name
        self.plants: list[Plant] = []
        self.stats: GardenManager.GardenStats = self.GardenStats()
        GardenManager._gardens[owner_name] = self

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden."""
        self.plants.append(plant)
        self.stats.add_plant(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def help_grow(self) -> None:
        """Simulate growth for all plants."""
        print(f"{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(1)
            self.stats.record_growth(1)
            print(f"{plant.name} grew 1cm")

    def get_report(self) -> None:
        """Print the full garden report."""
        print(f"=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.get_info()}")
        print(self.stats.get_report())

    @classmethod
    def create_garden_network(cls) -> dict[str, "GardenManager"]:
        """Return the dictionary of all created gardens."""
        return cls._gardens

    @staticmethod
    def validate_height(height: int) -> bool:
        """Check if height is valid (positive)."""
        return height > 0


def main():
    """Main function to test GardenManager."""
    print("=== Garden Management System Demo ===\n")

    alice_garden = GardenManager("Alice")

    oak = Plant("Oak Tree", 100, 365)
    rose = FloweringPlant("Rose", 25, 30, "red")
    rose.bloom()
    sunflower = PrizeFlower("Sunflower", 50, 45, "yellow", 10)
    sunflower.bloom()

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    print()
    alice_garden.help_grow()
    print()

    alice_garden.get_report()

    print("\nHeight validation test:", GardenManager.validate_height(10))
    print(f"Total gardens managed: "
          f"{len(GardenManager.create_garden_network())}")


if __name__ == "__main__":
    main()
