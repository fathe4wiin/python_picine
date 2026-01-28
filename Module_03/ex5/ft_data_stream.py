import time

def fibonacci_gen():
    a = 0
    b = 1
    while True:
        yield a
        temp = a
        a = b
        b = temp + b


def prime_gen():
    n = 2
    while True:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            yield n
        n += 1

def lol_event_stream():
    events = [
        (1, "Ahri",    7, "kill",      "mid",  False, False),
        (2, "Yasuo",   11, "death",    "baron", True, False),
        (3, "Zed",     12, "first blood", "top", False, False),
        (4, "Jinx",     9, "turret destroyed", "bot", False, False),
        (5, "Thresh",   13, "assist",   "bot",  False, False),
        (6, "Lux",      15, "ultimate", "mid",  False, False),
        (7, "Ezreal",   16, "dragon steal", "dragon", True, False),
        (8, "Lee Sin",  14, "insec",    "none", False, False),
        (9, "Ashe",     18, "pentakill","mid",  False, True),
        (10, "Darius",  10, "shutdown", "top",  False, False),
    ]
    index = 0
    while index < len(events):
        yield events[index]
        index += 1

def main():
    print("=== Game Data Stream Processor ===\n")
    count = 0
    for _ in lol_event_stream():
        count += 1
    print(f"Processing {count} game events...\n")

    event = lol_event_stream()
    for _ in range(1, 6):
        num, champ, level, event_type, lane, is_jungle_event, is_legendary_event = next(event)
        output = f"Event {num}: {champ} (level {level}), {event_type} on {lane}"
        if is_jungle_event:
            output += " [Jungle event]"
        if is_legendary_event:
            output += " [Legendary event]"
        print(output)
    print("...\n")
    print("=== Stream Analytics ===")
    event = lol_event_stream()

    high_level = 0
    jungle = 0
    legendary = 0
    before = time.time()

    for _ in range(1, count + 1):
        num, champ, level, event_type, lane, is_jungle_event, is_legendary_event = next(event)
        if level >= 10:
            high_level += 1
        if is_jungle_event:
            jungle += 1
        if is_legendary_event:
            legendary += 1

    print(f"Total events: {count}")
    print(f"High level player events (level >= 10): {high_level}")
    print(f"Jungle events: {jungle}")
    print(f"Legendary events: {legendary}")
    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {time.time() - before:.9f} seconds\n")
    print("=== Generator Demonstration ===")
    fib = fibonacci_gen()
    print("Fibonacci sequence (first 10): ", end= "")
    for i in range(1, 11):
        print(f"{next(fib)}", end="")
        if i < 10:
            print(", ", end="")
    prime = prime_gen()
    print("\nPrime numbers (first 10): ", end="")
    for i in range(1, 11):
        print(f"{next(prime)}", end="")
        if i < 10:
            print(", ", end="")


if __name__ == "__main__":
    main()
