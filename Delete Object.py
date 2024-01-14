class Demo:
    def __init__(self):
       print("Constructor Created")
    def __del__(self):
        print("Destructor Called")
s1=Demo()
s2=Demo()
del s1 #object Deleted
#s2.__del__ Destructor
