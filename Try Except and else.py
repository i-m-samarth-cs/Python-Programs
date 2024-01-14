try:
    fh=open("Sample.txt",'rt+')
    fh.write("This is my Test File")
except IOError:
    print("Error cant find File")
else:
    print("Written Content in the File")
    fh.close()
