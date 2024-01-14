dict2={'name':'SAM','Age':18,'Marks':90.44}

print(dict2)
print("Name is:",dict2['name'])

for i in dict2:
    print("Key is:",i," value is :",dict2[i])

dict2['city']="Dhule"
print(dict2)

d1={'a':1,'b':2,'c':3,'d':4,'e':5}
d1.pop()

del(d1['b'])

del d1

len(dict2)
print('name' in dict2)
