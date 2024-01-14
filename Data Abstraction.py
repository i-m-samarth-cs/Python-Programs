class Color:
    @abstractmethod
    def showColor(self):
        none
class Red(Color):
    def showColor(self):
        print("red")
class Green(Color):
    def showColor(self):
        print("Green")
def main():
    r=Red()
    r.showColor()
    b=Green()
    b.showColor()
    if __name__=='__main__':
        main()
