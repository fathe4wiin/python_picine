class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(
            self,
            name: str,
            water_level: int,
            sunlight_hours: int) -> None:
        self.name: str = name
        self.water_level: int = water_level
        self.sunlight_hours: int = sunlight_hours


class GardenManager:
    def __init__(self) -> None:
        self.plants: list[Plant] = []

    def add_plant(
            self,
            name: str,
            water_level: int,
            sunlight_hours: int) -> None:
        try:
            self.check_name(name)
            plant = Plant(name, water_level, sunlight_hours)
            self.plants.append(plant)
            print(f"Added {name} successfully")
        except ValueError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self, water_level: int) -> None:
        if water_level < len(self.plants):
            raise WaterError("Not enough water in tank")
        print("Watering plants...")
        system_open: bool = False
        try:
            print("Opening watering system")
            system_open = True
            for plant in self.plants:
                if not isinstance(plant, Plant):
                    raise PlantError(f"Cannot water {plant} - invalid plant!")
                plant.water_level += 1
                print(f"Watering {plant.name} - success")
        except PlantError as e:
            print(f"Error watering plants: {e}")
        finally:
            if system_open:
                print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        print("Checking plant health...")
        for plant in self.plants:
            try:
                self.check_name(plant.name)
                self.check_water_level(plant.water_level)
                self.check_sunlight(plant.sunlight_hours)
                print(
                    f"{plant.name}: healthy (water: {plant.water_level},"
                    f" sun: {plant.sunlight_hours})")
            except ValueError as e:
                print(f"Error checking {plant.name}: {e}")

    def check_name(self, plant_name: str) -> None:
        if not plant_name:
            raise ValueError("Plant name cannot be empty!")

    def check_water_level(self, water_level: int) -> None:
        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")

    def check_sunlight(self, sunlight_hours: int) -> None:
        if sunlight_hours < 2:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)")
        if sunlight_hours > 12:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)")


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    print()
    manager = GardenManager()
    print("Adding plants to garden...")

    manager.add_plant("tomato", 5, 8)
    manager.add_plant("lettuce", 10, 12)
    manager.add_plant("", 5, 8)
    print()

    try:
        manager.water_plants(2)
    except WaterError as e:
        print(f"Caught GardenError: {e}")
    print()

    manager.check_plant_health()
    print()

    print("Testing error recovery...")
    try:
        manager.water_plants(1)
    except WaterError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...")
    print()
    print("Garden management system test complete!")


def main() -> None:
    test_garden_management()


if __name__ == "__main__":
    main()
