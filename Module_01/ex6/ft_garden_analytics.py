class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    
    def grow(self, amount=1):
        self.height += amount
    
    def get_info(self):
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False
    
    def bloom(self):
        self.is_blooming = True
    
    def get_info(self):
        status = "blooming" if self.is_blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers ({status})"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, prize_points):
        super().__init__(name, height, age, color)
        self.prize_points = prize_points
    
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Prize points: {self.prize_points}"


class GardenManager:
    class GardenStats:
        def __init__(self):
            self.plants_added = 0
            self.total_growth = 0
            self.regular_count = 0
            self.flowering_count = 0
            self.prize_count = 0
        
        def add_plant(self, plant):
            self.plants_added += 1
            if isinstance(plant, PrizeFlower):
                self.prize_count += 1
            elif isinstance(plant, FloweringPlant):
                self.flowering_count += 1
            else:
                self.regular_count += 1
        
        def record_growth(self, amount):
            self.total_growth += amount
        
        def get_report(self):
            return (f"Plants added: {self.plants_added}, "
                   f"Total growth: {self.total_growth}cm\n"
                   f"Plant types: {self.regular_count} regular, "
                   f"{self.flowering_count} flowering, "
                   f"{self.prize_count} prize flowers")
    
    _gardens = {}
    
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.plants = []
        self.stats = self.GardenStats()
        GardenManager._gardens[owner_name] = self
    
    def add_plant(self, plant):
        self.plants.append(plant)
        self.stats.add_plant(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")
    
    def help_grow(self):
        print(f"{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(1)
            self.stats.record_growth(1)
            print(f"{plant.name} grew 1cm")
    
    def get_report(self):
        print(f"=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.get_info()}")
        print(self.stats.get_report())
    
    @classmethod
    def create_garden_network(cls):
        return cls._gardens
    
    @staticmethod
    def validate_height(height):
        return height > 0
    
    @staticmethod
    def calculate_garden_score(garden):
        score = 0
        for plant in garden.plants:
            score += plant.height
            if isinstance(plant, FloweringPlant) and plant.is_blooming:
                score += 10
            if isinstance(plant, PrizeFlower):
                score += plant.prize_points
        return score


def main():
    print("=== Garden Management System Demo ===\n")
    
    alice_garden = GardenManager("Alice")
    alice_garden.add_plant(Plant("Oak Tree", 100, 365))
    alice_garden.add_plant(FloweringPlant("Rose", 25, 30, "red"))
    alice_garden.add_plant(PrizeFlower("Sunflower", 50, 45, "yellow", 10))
    
    print()
    alice_garden.help_grow()
    
    print()
    for plant in alice_garden.plants:
        if isinstance(plant, FloweringPlant):
            plant.bloom()
    
    print()
    alice_garden.get_report()
    
    print()
    print(f"Height validation test: {GardenManager.validate_height(100)}")
    
    bob_garden = GardenManager("Bob")
    bob_garden.add_plant(Plant("Fern", 50, 60))
    bob_garden.add_plant(FloweringPlant("Tulip", 20, 25, "pink"))
    
    alice_score = GardenManager.calculate_garden_score(alice_garden)
    bob_score = GardenManager.calculate_garden_score(bob_garden)
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    
    network = GardenManager.create_garden_network()
    print(f"Total gardens managed: {len(network)}")


if __name__ == "__main__":
    main()

