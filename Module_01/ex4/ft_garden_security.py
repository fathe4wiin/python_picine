from typing import Any


class SecurePlant:
    """
    A class representing a plant with secure data access.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a SecurePlant.
        """
        self.name: str = name
        print(f"Plant created: {self.name}")

    def set_height(self, height: int) -> None:
        """
        Securely set the height of the plant.

        Args:
            height (int): The height to set. Must be non-negative.
        """
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.height = height
            print(f"Height updated: {self.height}cm [OK]")

    def set_age(self, age: int) -> None:
        """
        Securely set the age of the plant.

        Args:
            age (int): The age to set. Must be non-negative.
        """
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.age = age
            print(f"Age updated: {self.age} days [OK]")

    def get_height(self) -> Any:
        """
        Get the height of the plant.
        """
        return getattr(self, 'height', "(N/A)")

    def get_age(self) -> Any:
        """
        Get the age of the plant.
        """
        return getattr(self, 'age', "(N/A)")

    def get_info(self) -> None:
        """
        Print the plant's information.
        """
        height = self.get_height()
        age = self.get_age()
        print(f"Current plant: {self.name.capitalize()} "
              f"({height}cm, {age} days)")


def main() -> None:
    """
    Main function to test the Garden Security System.
    """
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose")
    rose.set_height(25)
    rose.set_age(30)

    rose.set_height(-5)
    rose.set_age(-10)

    rose.get_info()


if __name__ == "__main__":
    main()
