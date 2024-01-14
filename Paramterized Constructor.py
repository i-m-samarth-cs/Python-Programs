class Student:
    def __init__(self,name):
        print("Parametrized Constructor")
        self.name=name
    def show(self):
        print("Hello ",self.name)
s1=Student("Samarth")
s1.show()
