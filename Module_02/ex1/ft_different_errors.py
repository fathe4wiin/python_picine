def test_error_types() -> None:
    print("Testing multiple errors together...")
    try:
        10 / 0
        open("config.txt")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")


def garden_operations() -> None:
    my_data = {"apple": 1, "banana": 2}
    print("Testing ValueError...")
    try:
        int("iwkms")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    print()
    print("Testing ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    print()
    print("Testing FileNotFoundError...")
    try:
        open("config.json")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    print()
    print("Testing KeyError...")
    try:
        my_data["love"]
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    print()


def main() -> None:
    print("=== Garden Error Types Demo ===")
    print()
    garden_operations()
    test_error_types()
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    main()
