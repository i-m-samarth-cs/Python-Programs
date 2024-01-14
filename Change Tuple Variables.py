# Inputting the first tuple
tuple1 = tuple(input("Enter elements for the first tuple (space-separated): ").split())

# Inputting the second tuple
tuple2 = tuple(input("Enter elements for the second tuple (space-separated): ").split())

# Interchanging the tuples
temp = tuple1
tuple1 = tuple2
tuple2 = temp

# Printing the updated tuples
print("First tuple after interchange:", tuple1)
print("Second tuple after interchange:", tuple2)
