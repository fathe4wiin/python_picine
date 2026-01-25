class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age


def water_plants(plant_list: list) -> None:
    system_open: bool = False
    try:
        print("Opening watering system")
        system_open = True
        for plant in plant_list:
            if not isinstance(plant, Plant):
                raise PlantError(f"Cannot water {plant} - invalid plant!")
            print(f"WATERING: The {plant.name} is receiving water.")
    except PlantError as e:
        print(f"ERROR: {e}")
    finally:
        if system_open:
            print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print()

    valid_plants = [
        Plant("Rose", 15, 2),
        Plant("Tulip", 10, 1),
        Plant("Sunflower", 50, 3)
    ]

    invalid_plants = [
        Plant("Cactus", 5, 5),
        None,
        Plant("Fern", 20, 4)
    ]

    print("Testing normal watering...")
    water_plants(valid_plants)
    print("Watering completed successfully!")
    print()
    print("Testing with error...")
    water_plants(invalid_plants)
    print()
    print("Cleanup always happens, even with errors!")


def main() -> None:
    print("=== Garden Watering System ===")
    test_watering_system()


if __name__ == "__main__":
    main()
