class Father:
    def display1(self):
        print("Father")
class Mother:
    def display2(self):
        print("Mother")
class Son(Father,Mother):
    def display3(self):
        print("Son")
s1=Son()
s1.display3()
s1.display2()
s1.display1()
