class Vehicle:
    name="Maruti"
    def display(self):
        print("Name=",self.name)
class Category(Vehicle):
    price=2000
    def dis(self):
        print("Price= Rs",self.price)
c=Category()
c.display()
c.dis()
