def ft_count_harvest_recursive():
    t = int(input("Days until harvest: "))
    d = 1

    def count(t, d):
        if (d > t):
            print("Harvest time!")
        else:
            print(f"Day {d}")
            count(t, d + 1)

    count(t, d)


ft_count_harvest_recursive(int char ft_count_harvest_recursive_2())