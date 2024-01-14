tuple1=(1,2,3,4,5)
tuple2=(2,"SAM",4.5)
print(tuple1)

print(tuple1[1])

for ele in tuple2:
    print(ele)

slice_tuple=tuple1[1:4]
print(slice_tuple)

del tuple2
tuple3=(6,7,8)
tuple4=tuple1+tuple3

tuple3*3
print(tuple3)

a=len(tuple1)
print(a)
