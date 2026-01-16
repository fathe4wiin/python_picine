def ft_water_reminder():
    t = int(input("Days since last watering: "))
    if t > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
