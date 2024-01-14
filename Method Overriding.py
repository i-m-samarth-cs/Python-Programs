class Parent:
    def __init__(self):
        self.age=45
    def display(self):
        print("Age:",self.age)
class Child:
    def display(self):
        self.age=25
        print("Age=",self.age)
p=Parent()
c=Child()
p.display()
c.display()
