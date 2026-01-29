import sys


def main():
    print("=== Command Quest ===")
    if len(sys.argv) < 2:
        print("No arguments provided!")
    else:
        print(f"Arguments Count: {len(sys.argv) - 1}")
    print()
    print(f"Program name: {sys.argv[0]}")
    count: int = 1
    for arg in sys.argv[1:]:
        print(f"Argument {count}: {arg}")
        count += 1


if __name__ == "__main__":
    main()
