import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print()
    sys.stdout.write("Input Stream active. Enter archivist ID: ")
    sys.stdout.flush()

    file_name: str = sys.stdin.readline().rstrip("\n")
    sys.stdout.write("Input Stream active. Enter status report: ")
    sys.stdout.flush()

    data: str = sys.stdin.readline()
    print()
    sys.stdout.write(f"[STANDARD] Archive status from {file_name}: {data}")
    try:
        f = open(file_name, "a")
    except BaseException:
        sys.stderr.write("[ALERT] Data transmission FAILED\n")
        return

    sys.stderr.write(
        "[ALERT] System diagnostic: Communication channels verified\n")
    f.write(data)
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    print()

    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()
