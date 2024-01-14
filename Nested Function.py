def outer(num1):
    def inner(num1):
        return num1+1
    num2=inner(num1)
    print(num1,num2)
outer(15)
