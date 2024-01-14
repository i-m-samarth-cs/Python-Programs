try:
    age=int(input("Enter your Age:"))
    if age<18:
        raise Exception
    else:
        print("You are eligible for Selection")
        
except Exception:
        print("Too Small Ty Again")
    
