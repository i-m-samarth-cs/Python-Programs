class GrandFather:
    def display1(self):
        print("Grand Father")
class Father(GrandFather):
    def display2(self):
        print("Father")
class Son(Father):
    def display3(self):
        print("Son")
s1=Son()
s1.display3()
s1.display2()
s1.display1()

