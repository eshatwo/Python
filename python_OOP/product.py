class Product:
    def __init__(self, price, item_name, weight, brand):
          self.price = price
          self.item_name = item_name
          self.weight = weight
          self.brand = brand
          self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self
    
    def add_tax(self, tax):
        self.price = self.price * tax
        return self

    def return_item(self, reason_for_return):
        if (reason_for_return == "defective"):
            self.status = "defective"
            self.price = 0
        if (reason_for_return == "like_new"):
            self.status = "for sale"
        if (reason_for_return == "opened"):
            self.status = "used"
            self.price = self.price * .80
        return self
        
    def display_info(self):
        disp = {
            "Price" : self.price,
            "Item Name" : self.item_name,
            "Weight" : self.weight,
            "Brand" : self.brand,
            "Status" : self.status
        }
        print(disp)
        return self

product1 = Product(2000, "Purse", "2lbs", "Gucci")

product1.add_tax(1.0825).display_info().return_item("opened").display_info()


