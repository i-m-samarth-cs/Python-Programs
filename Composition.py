class Marks:
    def __init__(self,theory,pract):
        self.pract=pract
        self.theory=theory
    def calculate(self):
        return (self.theory + self.pract)
class Student:
    def __init__(self,roll,name,th,pract):
        self.roll=roll
        self.name=name
        self.th=th
        self.pract=pract
        self.obj_Mar=Marks(self.theory,self.pract)
    def total(self):
        return self.obj_Mar.calculate()
s=Student(101,'AAA',70.25,25.00)
print("Roll no:",s.roll)
print("Name:",s.name)
print("Total:",s.total())
