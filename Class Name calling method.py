class A:
    def display():
        print("Executing in Super Class")
class B:
    def display():
        print("Begin of Sub Class")
        A.display()
        print("End")
obj=A()
A.display()
obj=B()
B.display()
