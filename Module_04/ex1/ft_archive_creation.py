def main() -> None:
    data: list[str] = ["[ENTRY 001] New quantum algorithm discovered",
            "[ENTRY 002] Efficiency increased by 347%",
            "[ENTRY 003] Archived by Data Archivist trainee"]

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print()

    file_name: str = "new_discovery.txt"
    print(f"Initializing new storage unit: {file_name}")
    try:
        f = open(file_name, "w")
    except BaseException:
        print("ERROR, unable to create the file")
        return
    print("Storage unit created successfully...")

    print("\nWriting data...")
    for s in data:
        print(s)
        f.write(s + "\n")
    print()
    f.close()
    print("Data inscription complete. file CLOSED.")
    print(f"Archive '{file_name}' ready for storage.")


if __name__ == "__main__":
    main()
