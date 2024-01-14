import re
str="I am Ironman"
a=re.search("^I.*Man$",str)
if(a):
    print("Match Found")
else:
    print("No Match")
a1=str.split()
print(a1)
