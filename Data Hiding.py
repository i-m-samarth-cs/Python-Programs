class Counter:
    __secret = 10  #Private Variable
    def count(self):
        self.count==1
        print("Count=",self.__secret)
c1=Counter()
c1.count()
print("Total Count=",c1.__secret)
    
