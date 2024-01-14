def perfect(num):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    if sum==n:
        print("Perfect Number")
    else:
        print("Not Perfect Number")
n=int(input("Enter any Number:"))
perfect(n)
