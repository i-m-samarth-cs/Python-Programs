class Rectangle:
    def __init__(self):
        self.length=10
        self.width=12
    def rectange_area(self):
        return self.length*self.width
obj=Rectangle()
print("Area=",obj.rectange_area())
