def Reverse(num):
    rev=0
    while(num>0):
        rem=num%10
        rev=(rev*10)+rem
        num=num/10
    return rev
a=int(input("Enter any Number:"))
print("Reverse of Number ",a,"is:",Reverse(a))
