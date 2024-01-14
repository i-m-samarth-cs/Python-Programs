class Student:
    def __init__(self,a=18,b="CS"):
        self.a=a
        self.b=b
    def display(self):
        print("Age:",self.a)
        print("Subject:",self.b)
s1=Student()
s1.display()
s2=Student(19,"IT")
s2.display()
