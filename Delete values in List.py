list2=['a','b','c','d','e']
print(list2)
val=list2.pop(1)
print(val)
print(list2)

val=list2.pop()
print(val)

list2.remove('d')
print(list2)

del list2[0:1]
print(list2)

list2.clear()
print(list2)
