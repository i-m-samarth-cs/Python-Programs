class Student:
    __a=10  #Private
    b=20    #Public
    _c=30   #Protected
    def __show(self):
        print("Private Method")
    def show2(self):
        print("Public Method")
        print("A=",self.__a)
s1=Student()
print("B=",s1.b)
s1.show2()
