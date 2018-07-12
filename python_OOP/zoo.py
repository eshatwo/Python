class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def addDog(self, name):
        self.animals.append( Dog(name) )
    def addDragon(self, name):
        self.animals.append( Dragon(name) )
    def printAllHealth(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.displayHealth()

class Dog(Zoo):
    def __init__(self, name):
        super().__init__(name)
        self.health = 150
    
    def pet(self):
        self.health += 5
        return self

     def display_health(self):
        print("I am a Dog")
        return super().display_health()

class Dragon(Zoo):
    def __init__(self, name):
        super().__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        print("I am a Dragon")
        return super().display_health()

zoo1 = Zoo("John's Zoo")
zoo1.addDog("Tracy")
zoo1.addDog("Doggy")
zoo1.addDragon("Draggy")
zoo1.addDragon("Dragoon")
zoo1.printAllHealth()
