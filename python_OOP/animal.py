class Animal:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self
    
    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print(self.health)
        return self

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.health = 150
    
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        print("I am a Dragon")
        return super().display_health()


d1 = Dog("Cashew")
dr1 = Dragon("Fire")
animal1 = Animal("John")


d1.walk().walk().walk().run().run().pet().display_health()
dr1.fly().fly().fly().display_health()
animal1.walk().walk().run().display_health()

