dict2={'name':'SAM','Age':21,'Marks':90.44}

print("All Items in Dictionary:\n",dict2.items())
print("All Keys in Dictionary:\n",dict2.keys())

print("All values in Dictionary:'n",dict2.values())

dict3=dict2.copy()
print(dict3)

dict2.setdefault(1,'SAMARTH')
print(dict2)

dict4={5:"Arjun",6:"Ram"}
dict2.update(dict4)
print(dict2)

dict3.clear()

print("Age:",dict2.get('Age'))

dict2.ksort()
print(dict2)

t1=list(dict2.items())
print(t1)
