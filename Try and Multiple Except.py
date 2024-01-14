try:
    a=int(input("Enter Value of A:"))
    b=int(input("Enter Value of B:"))
    c=a/b
except ValueError:
    print("You have Entered Wrong Data")
except ZeroDivisionError:
    print("Cannot Divide by Zero")
    
