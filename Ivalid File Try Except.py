name=input("Entet File name to Open")
try:
    f=open(name,"r")
    print(f.read())
except FileNotFoundError:
    print("No Such File")
