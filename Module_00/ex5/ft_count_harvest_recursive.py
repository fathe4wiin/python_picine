def count(t, d):
    if (d > t):
        print("Harvest time!")
    else:
        print(f"Day {d}")
        count(t, d + 1)


def ft_count_harvest_recursive():
    t = int(input("Days until harvest: "))
    d = 1
    count(t, d)
