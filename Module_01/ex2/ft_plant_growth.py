class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        self.last_growth = 0

    def get_info(self):
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age} days old")

    def grow(self, growth_amount):
        self.height += growth_amount
        self.last_growth = growth_amount
    def age_one_day(self):
        self.age += 1

def main():
    print("=== Day 1 ===")
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    rose.get_info()
    sunflower.get_info()
    cactus.get_info()

    for day in range(1, 28):

        rose.grow(2)
        sunflower.grow(5)
        cactus.grow(1)

        rose.age_one_day()
        sunflower.age_one_day()
        cactus.age_one_day()

        if (day % 7 == 0):
            print(f"=== Day {day} ===")
            rose.get_info()
            sunflower.get_info()
            cactus.get_info()
            print(f"growth this week - Rose: +{rose.last_growth}cm, Sunflower: +{sunflower.last_growth}cm, Cactus: +{cactus.last_growth}cm")

if __name__ == "__main__":
    main()