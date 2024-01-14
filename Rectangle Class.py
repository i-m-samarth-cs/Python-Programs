class Rectangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        return self.l*self.w
r=Rectangle(2,10)
print(r.area())
