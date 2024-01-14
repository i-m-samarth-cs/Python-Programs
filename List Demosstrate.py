list1=[1,2,3,'SAM','john',78.9]
print(list1)

print(list1[1])

i=0
while i<list1.__len__():
    print(list1[i])
    i=i+1

print(list1[-1])

for ele in list1:
    print(ele)

slice_list=list1[2:5]
print(slice_list)

list1.append('Mike')
print(list1)

list1.remove

a=1 in list1

list1[4]='Boss'
a=list1.__len__()
print("Length =",a)

for item in enumerate(list1):
    print(item)
