PI=22/7
height=float(input("Enter Height:"))
rad=float(input("Radius of Cylinder:"))
volume=PI*rad*rad*height

sur_area=((2*PI*rad)*height)+((PI*rad**2)*2)
print("Volume :",volume)
print("Surface Area:",sur_area)
