def leap(year):
    if((year%4==0) and (year%100!=0)):
        print(year,"is Leap Year")
    elif(year%400==0):
        print(year,"is Leap Year")
    elif(year%100==0):
        print(year,"is not Leap Year")
    else:
        print(year,"is not Leap Year")
year=int(input("Enter Year:"))
leap(year)
        
