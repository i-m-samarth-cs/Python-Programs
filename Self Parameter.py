class Demo:
    roll=0
    name=""
    def accept(self):
        print("Enter Roll Number:")
        self.roll=int(input())
        print("Enter your name:")
        self.name=input()
    def display(self):
        print("Roll No:",self.roll)
        print("Name:",self.name)
s1=Demo()
s1.accept()
s1.display()
