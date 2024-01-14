set1={'x','y','z'}
print(set1)

set1.add('m')
print(set1)

s1=set('abc')
print(s1)

for count in set1:
    print(count)
set2={1,2,3,4,5,6}
set2.pop()
print(set2)

set2.remove(3)
print(set2)

set1.update('E')
print(set1)

set3=frozenset({'a','b','c'})
print(set3)

set2.discard(4)
print(set2)
