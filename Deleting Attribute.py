class Test:
    x=5
    y=10
    def display(self):
        print("X=",self.x)
        print("Y=",self.y)
t1=Test()
t1.display()
del Test.x
print("X=",t1.x)
print("Y=",t1.y)
