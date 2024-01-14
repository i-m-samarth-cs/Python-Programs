n=int(input("Enter Number:"))
for i in range(2,n+1):
    if n%i==0:
        break
if i==n:
    print(n,"is Prime")
else:
    print(n,"not Prime")
