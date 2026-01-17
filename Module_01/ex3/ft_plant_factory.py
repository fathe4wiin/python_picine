class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        
    def creation_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def main():
    plant_data = [
    ("Rose", 25, 30),
    ("Oak", 200, 365),
    ("Cactus", 5, 90),
    ("Sunflower", 80, 45),
    ("Fern", 15, 120),
    ]

    plants = []

    for name, height, age in plant_data:
        plant = Plant(name, height, age)
        plants.append(plant)

    print("=== Plant Factory Output ===")
    for plant in plants:
        plant.creation_info()
    print(f"Total plants created: {len(plants)}")

if __name__ == "__main__":
    main()