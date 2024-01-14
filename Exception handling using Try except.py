print("Main Area Starts")
a=[10,20,30]
try:
    print("Second:",a[1])
    print("Fourth:",a[3])
except IndexError:
    print("Exception Occurs Invalid Index")
print("Main Area Ends")
