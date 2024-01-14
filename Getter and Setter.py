class Car:
    def get(self,color,style):
        self.color=color
        self.style=style
    def put(self):
        print(self.color)
        print(self.style)
c=Car()
c.get("Sedan","Black")
c.put()
