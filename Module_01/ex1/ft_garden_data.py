class Plant:
    """
    A class to represent a plant in the garden.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a new Plant instance.

        Args:
            name (str): The name of the plant.
            height (int): The height of the plant in cm.
            age (int): The age of the plant in days.
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> None:
        """
        Print the information about the plant.
        """
        print(f"{self.name.capitalize()}: {self.height}cm, "
              f"{self.age} days old")


def main() -> None:
    """
    Main function to demonstrate Plant class usage.
    """
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    rose.get_info()
    sunflower.get_info()
    cactus.get_info()


if __name__ == "__main__":
    main()
