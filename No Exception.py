while true:
    try:
        a=int(input("Enter a Number:"))
        div=10/a
        break
    except:
        print("Error Occured")
        print("Please Enter Valid Value")
        print()
print("Division is:",div)
