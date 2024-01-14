class Person:
    def __init__(self,roll,name,age):
        self.roll=roll
        self.name=name
        self.age=age
        print("Student Obj Created")
p1=Person(1,"SAM",40)
print("Roll No:",p1.roll)
print("Name:",p1.name)
print("Age:",p1.age)
