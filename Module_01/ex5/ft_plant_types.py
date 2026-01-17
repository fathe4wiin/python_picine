class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

class Flower(Plant):
    def __init__(self, name, height, age, color, bloom):
        super().__init__(name, height, age)
        self.color = color
        self.bloom = bloom
    
    def get_info(self):
        return f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color.lower()} color\n{self.name} is blooming beautifully!"

class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter, products_shade):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.products_shade = products_shade
    
    def get_info(self):
        shade_area = self.height * self.trunk_diameter / 100 if self.products_shade else 0
        return f"{self.name} (Tree): {self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter\n{self.name} provides {shade_area} square meters of shade"

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
    
    def get_info(self):
        return f"{self.name} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season.lower()} harvest\n{self.name} is rich in {self.nutritional_value}"

def main():
    print("=== Garden Plant Types ===")
    Rose = Flower("Rose", 30, 45, "Red", "Spring")
    Tulip = Flower("Tulip", 25, 30, "Yellow", "Spring")
    
    Oak = Tree("Oak", 500, 200, 80, True)
    Maple = Tree("Maple", 400, 150, 70, True)
    
    Tomato = Vegetable("Tomato", 60, 90, "Summer", "Vitamin C")
    Carrot = Vegetable("Carrot", 30, 120, "Fall", "Beta-carotene")
    
    plants = [Rose, Tulip, Oak, Maple, Tomato, Carrot]
    
    for plant in plants:
        print(plant.get_info())
        print()

if __name__ == "__main__":
    main()