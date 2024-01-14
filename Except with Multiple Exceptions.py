i=0
while i<=1:
    try:
         a=15/i
         print("Division is:",a)
         print("Value of B=",b)
    except (ZeroDivisionError,NameError):
        print("\n",sys.exe_info(),"Occured and Handled")
    i=i+1
        
   
