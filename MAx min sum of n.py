list1=[]
n=int(input("enter the value of list"))
for i in range(n):
      print("Enter any Element:")
      new=int(input())
      list1.append(new)

print(list1)
print("Max")
print(max(list1))

print("Min")
print(min(list1))

print("Sum")
print(sum(list1))

b=sum(list1)
print("Avg")
avg=b/n

print(avg)
