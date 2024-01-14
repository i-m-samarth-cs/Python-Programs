def isPrime(num):
    if num>1:
        for i in range(2,num):
            if((num%i)==0):
                print(num,"is not Prime")
                print(i,"times",num/i,"is",num)
                break
            else:
                print(num,"is Prime")
    else:
        print(num,"is not Prime")
num=int(input("Enter any Number:"))
isPrime(num)
