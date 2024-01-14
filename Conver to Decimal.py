binary=list(input("Enter a Binary Number:"))
value=0
for i in range(len(binary)):
    digit=binary.pop()
    if digit=='1':
        value=value+pow(2,i)
print("Decimal Value:",value)
