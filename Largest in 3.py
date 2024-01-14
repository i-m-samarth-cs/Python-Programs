x=10
y=5 
z=15

if(x>y) and (x>z):
    l=x
elif(y>x) and (y>z):
    l=y
elif(z>x) and (z>y):
    l=z
else:
    print("All are Equal")

print("Largeest:",l)