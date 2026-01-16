def ft_count_harvest_iterative():
    t = int(input("Days until harvest: "))
    d = 1
    while d <= t:
        print(f"Day {d}")
        d += 1
    print("Harvest time!")


ft_count_harvest_iterative()
