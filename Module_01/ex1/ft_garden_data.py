class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age} days old")


def main():
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    rose.get_info()
    sunflower.get_info()
    cactus.get_info()

if __name__ == "__main__":
    main()