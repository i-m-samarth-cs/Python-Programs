import itertools
num=[1,2,34]
list(itertools.combinations(num,3))
print(num)
print(list(itertools.product(num,repeat=2)))
print(list(itertools.repeat(10,3)))
