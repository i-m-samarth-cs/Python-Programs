print("Enter 1st Number:")
b=int(input())
a=int(input("Enter 2nd Number:"))
rem=a%b
while rem !=0:
    a=b
    b=rem
    rem=a%b
print("GCD:",b)
