n=int(input("Enter value of n:"))
a=0
b=1
i=0
print("Fibonacci")
while i<n:
    print(a)
    print(b)
    c=a+b
    a=b
    b=c
    i=i+1
