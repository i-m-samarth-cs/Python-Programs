from datetime import datetime

# Input date 1 from the user
date1_input = input("Enter date 1 (YYYY-MM-DD): ")
date1 = datetime.strptime(date1_input, "%Y-%m-%d")

# Input date 2 from the user
date2_input = input("Enter date 2 (YYYY-MM-DD): ")
date2 = datetime.strptime(date2_input, "%Y-%m-%d")

# Compare the dates
if date1 < date2:
    print("Date 1 is earlier than Date 2.")
elif date1 > date2:
    print("Date 1 is later than Date 2.")
else:
    print("Date 1 is the same as Date 2.")
