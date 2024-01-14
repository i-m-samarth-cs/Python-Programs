def factorial(num):
    if(num==1):
        return num
    else:
        return num*factorial(num-1)
num=int(input("Enter any Number:"))
if(num<0):
    print("Cannot Find Factorial of Neagtive Numbers:")
elif(num==0):
    print("Factorial of 0 is 1")
else:
    print("Factorial of ",num,"is",factorial(num))
