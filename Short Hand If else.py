print("enter 3 values:")
n1=int(input())
n2=int(input())
n3=int(input())

lar=n1 if n1>n2 and n1>n3  else n2 if n2>n3 else n3
print(lar," is Largest")