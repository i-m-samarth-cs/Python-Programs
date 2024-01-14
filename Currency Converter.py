def dolrup():
    dollars=int(input("Please Enter Dollars:"))
    rupees=dollars*80
    print("Dollar:",dollars)
    print("Rupees:",rupees)
def euro_rup():
    euro=int(input("Please Enter Euros:"))
    rupees=euro*79.30
    print("Euro:",euro)
    print("Rupees:",rupees)
def menu():
    print("1.Dollar to Rupees")
    print("2.Euro to Rupees")
    print("3.Exit")
    choice=int(input("Select Choice:"))
    if choice==1:
        dolrup()
    if choice==2:
        euro_rup()
    if choice==3:
        exit("Good Bye")

menu()
               
