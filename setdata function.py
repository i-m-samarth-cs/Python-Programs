class Father:
    def setdata(self,value):
        self.data=value
    def display(self):
        print(self.data)
class Child(Father):
    def display(self):
        print("Info is="%s ,%self.data)
a=Child()
)a.setdata(80)
a.display()
              
