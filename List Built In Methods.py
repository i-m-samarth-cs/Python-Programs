
list1=[1,2,3,4,5,"Sam","Ram"]
print(list1.index(5))

a=list1.count(3)
print("3 is Ocuured ",a," times")

list2=list1.copy()
print("Copied List is:",list2)

b=len(list1)
print(b)

#/*z=max(list1)
#print(z)
#y=min(list1)
#print(y)
#*/

print("Sum of Elements",sum(list2))

str="HEllo"
list3=list(str)
print(list3)

msg="I#Love#GPD"
list4=msg.split("#")
print(list4)

ch="@"
ch.join(list3)
