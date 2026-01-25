class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_name(plant_name: str) -> None:
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")


def check_water_level(water_level: int) -> None:
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")


def check_sunlight(sunlight_hours: int) -> None:
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)")


def check_plant_health(
        plant_name: str,
        water_level: int,
        sunlight_hours: int) -> str:
    check_name(plant_name)
    check_water_level(water_level)
    check_sunlight(sunlight_hours)
    return (f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")
    print()
    print("Testing good values...")
    try:
        result = check_plant_health("tomato", 5, 8)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 8)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 8)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    print("All error raising tests completed!")


def main() -> None:
    test_plant_checks()


if __name__ == "__main__":
    main()
