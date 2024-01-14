basic=float(input("Enter Basic Salary:"))
hra=(basic*10)/100
ta=(basic*5)/100
gross=basic+hra+ta
print("Gross Salary is:",gross)
tax=(gross*2)/100
net_sal=gross-tax
print("Net Salary is:",net_sal)

      
