class Error(Exception):
    pass
class AgeSmallException(Error):
    pass
while True:
    try:
        age=int(input("Enter Your Age:"))
        if age<18:
            raise AgeSmallException
        else:
            print("Your are eligible for Election")
            break
    except AgeSmallException:
        print("Too Small to Vote")
        print()
        
        
