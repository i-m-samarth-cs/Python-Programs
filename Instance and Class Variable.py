class Sample:
    x=2     #Class Variable
    def get(self,y):    #Instance Variable
        self.y=y
s1=Sample()
s1.get(3)
print(s1.x," ",s1.y)
