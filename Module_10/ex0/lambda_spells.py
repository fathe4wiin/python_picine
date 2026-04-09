

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda key: key['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] > min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda name: f"*{name}*", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda m: m['power'])['power']
    min_power = min(mages, key=lambda m: m['power'])['power']
    all_powers = list(map(lambda m: m['power'], mages))
    avg_power = round(sum(all_powers) / len(all_powers), 2)

    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
    }


def main():
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Wooden Wand', 'power': 40, 'type': 'weapon'}
    ]

    mages = [
        {'name': 'Aria', 'power': 90, 'element': 'air'},
        {'name': 'Zane', 'power': 75, 'element': 'fire'},
        {'name': 'Lumina', 'power': 88, 'element': 'light'}
    ]

    spells = ["ignite", "heal", "smite"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    if len(sorted_artifacts) >= 2:
        a1, a2 = sorted_artifacts[0], sorted_artifacts[1]
        print(
            f"{
                a1['name']} ({
                a1['power']} power) comes before {
                a2['name']} ({
                    a2['power']} power)")

    print("\nTesting power filter (min 80)...")
    strong_mages = power_filter(mages, 80)
    for m in strong_mages:
        print(f"Mage {m['name']} passed the trial.")

    print("\nTesting spell transformer...")
    transformed = spell_transformer(spells)
    print("".join(transformed))

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"Stats: {stats}")


if __name__ == "__main__":
    main()
