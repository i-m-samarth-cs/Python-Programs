class Test:
    def sayHello(self):
        print("Hello")
t1=Test()
t2=Test()
t1.x=10   #Externally add x
print(t1.x)
print(t2.x)     #Not Available for t2
