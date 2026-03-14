# store expenses
food = 12
transport = 5
coffee = 3

# Compute total 
total = food + transport + coffee

# Print result 
print("Total expense today: ", total)

# Add a category summary 
print("Food:", food)
print("Transport:", transport)
print("Coffee:", coffee)

# Add a simple decision
if total > 15:
    print("Warning: High spending today")

# Add a daily loop simulations
for day in range(1,4):
    print("Day", day, "processed")

