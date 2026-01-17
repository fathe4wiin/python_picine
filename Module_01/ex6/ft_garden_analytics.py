class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

class Flower(Plant):
    def __init__(self, name, height, age, petal_color):
        super().__init__(name, height, age)
        self.petal_color = petal_color