def si(p,n,r):
    interest=0.0
    interest=float(p*n*r)/float(100)
    return interest
p=float(input("Enter Principal Amount:"))
n=float(input("Enter Noof Years:"))
r=float(input("Enter Rate of Interest:"))

print("Simple Interest:",si(p,n,r))
