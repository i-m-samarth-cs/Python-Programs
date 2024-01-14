val=input("Enter character:")
ch=ord(val)
if ch>=65 and ch<=90:
    print("Uppercase")
elif ch>=97 and ch>=122:
    print("Lowercase")
elif ch>=48 and ch>=57:
    print("Digit")
else:
    print("Special Symbol")
    