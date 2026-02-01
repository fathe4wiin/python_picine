def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    file_name: str = "ancient_fragment.txt"
    print(f"Accessing file: {file_name}")
    try:
        vfile = open(file_name)
    except FileNotFoundError:
        print("ERROR: File not found.")
        return
    print()
    print("RECOVERED DATA:")
    print(vfile.read())
    print()
    vfile.close()
    print("Data recovery complete. file CLOSED.")


if __name__ == "__main__":
    main()
