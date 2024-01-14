x=int(input("Enter 1st No:"))
y=int(input("Enter 2nd No:"))
try:
    res=x/y
except ZeroDivisionError:
    print("Division by Zero")
else:
    print("Result is",res)
finally:
    print("Execute Finally Close")
