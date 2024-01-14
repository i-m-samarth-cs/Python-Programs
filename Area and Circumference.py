class Circle:
    def __init__(self,rad):
        self.rad=rad
    def getArea(self):
        return 3.14*self.rad**2
    def getCircumference(self):
        return self.rad*2*3.14
c=Circle(5)
print("Area=",c.getArea())
print("Circumference",c.getCircumference())
