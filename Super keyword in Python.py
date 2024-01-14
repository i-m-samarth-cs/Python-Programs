class A:
    def display(self):
        print("Base Class")
class B(A):
    def display(self):
        super().display()
        print("Derived Class")
obj=B()
obj.display()
