import sys


def main():
    inventory = dict()

    if len(sys.argv) < 2:
        print("Error: No arguments provided")
        print("Correct form: item:quantity (for example: potion:3)")
        return

    try:
        for arg in sys.argv[1:]:
            if ':' in arg:
                parts = arg.split(':')
                key = parts[0]
                value = int(parts[1])
                inventory.update({key: value})
            else:
                raise ValueError(arg)
    except ValueError:
        print(f"Error: invalid argument '{arg}'")
        print("Correct form: item:quantity (for example: potion:3)")
        return

    print("\n=== Inventory System Analysis ===")

    total_items = 0
    for v in inventory.values():
        total_items += v
    print(f"Total items in inventory: {total_items}")

    unique_types = len(inventory.keys())
    print(f"Unique item types: {unique_types}")

    print("\n=== Current Inventory ===")
    for item, qty in inventory.items():
        percent = round(qty / total_items * 100, 2)
        if qty != 1:
            units = "units"
        else:
            units = "unit"
        print(f"{item}: {qty} {units} ({percent}%)")

    print("\n=== Inventory Statistics ===")
    vals = list(inventory.values())
    top_qty = max(vals)
    low_qty = min(vals)

    abundant_items = []
    scarce_items = []

    for k in inventory.keys():
        if inventory.get(k) == top_qty:
            abundant_items.append(k)
        if inventory.get(k) == low_qty:
            scarce_items.append(k)

    most_abundant = abundant_items[0]
    least_abundant = scarce_items[0]
    print(
        f"Most abundant: {most_abundant} ({
            inventory.get(most_abundant)} units)")
    print(
        f"Least abundant: {least_abundant} ({
            inventory.get(least_abundant)} units)")

    print("\n=== Item Categories ===")
    mod_cat = dict()
    scarce_cat = dict()
    for k, v in inventory.items():
        if v >= 5:
            mod_cat.update({k: v})
        else:
            scarce_cat.update({k: v})
    print(f"Moderate: {mod_cat}")
    print(f"Scarce: {scarce_cat}")

    print("\n=== Management Suggestions ===")
    restock = []
    for k in inventory.keys():
        if inventory.get(k) <= 1:
            restock.append(k)
    print(f"Restock needed: {restock}")

    print("\n=== Dictionary Properties Demo ===")
    keys_list = list(inventory.keys())
    values_list = list(inventory.values())
    print(f"Dictionary keys: {keys_list}")
    print(f"Dictionary values: {values_list}")
    found_sword = False
    for key in inventory.keys():
        if key == "sword":
            found_sword = True
    print(f"Sample lookup - 'sword' in inventory: {found_sword}")


if __name__ == "__main__":
    main()
