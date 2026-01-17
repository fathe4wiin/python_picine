class SecurePlant:
    def __init__(self, name):
        self.name = name
        print(f"Plant created : {self.name}")
    
    def Set_hieght(self, height):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print(f"Security Alert: negative height rejected")
        else:
            self.height = height
            print(f"Height updated: {self.height}cm [OK]")
    def Set_age(self, age):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print(f"Security Alert: negative age rejected")
        else:
            self.age = age
            print(f"Age updated: {self.age} days [OK]")
    def get_height(self):
        return getattr(self, 'height', "(N\A)")
    def get_age(self):
        return getattr(self, 'age', "(N\A)")
    
    def get_info(self):
        height = self.get_height()
        age = self.get_age()
        print(f"Current plant: {self.name.capitalize()} ({height}cm, {age} days old)")
    
def main():
    print("=== Garden Security System ===")
    Rose = SecurePlant("Rose")
    Rose.Set_hieght(25)
    Rose.Set_age(30)
    Rose.Set_hieght(-5)
    Rose.Set_age(-10)
    Rose.get_info()


if __name__ == "__main__":
    main()