class Car:
    def __init__(self, price, speed, fuel, milaege):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.milaege = milaege
        self.tax = 0
    def taxing(self):
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        return self
    def display_all(self):
        disp = {
            "Price" : self.price,
            "Speed" : self.speed,
            "Fuel" : self.fuel,
            "Milaege" : self.milaege,
            "Tax" : self.tax
        }
        print(disp)
        return self

car1 = Car(2000, "35mph", "Full", "15mpg")
car2 = Car(2000, "5mph", "Not Full", "105mpg")
car3 = Car(2000, "15mph", "Kind of Full", "95mpg")
car4 = Car(2000, "25mph", "Full", "25mpg")
car5 = Car(2000, "45mph", "Empty", "25mpg")
car6 = Car(20000000, "35mph", "Empty", "15mpg")

car1.taxing().display_all()
car2.taxing().display_all()
car3.taxing().display_all()
car4.taxing().display_all()
car5.taxing().display_all()
car6.taxing().display_all()