# Welcome message
print("Welcome to the Tip Calculator.")

# Total bill
bill = float(input("What was the total bill? £"))

# Tip percentage
percent = int(input("What percentage tip would you like to give: 10, 12, or 15? "))

# Number of people
people = int(input("How many people will split the bill? "))

# Calculation
amount = (bill / people) * (1 + (percent / 100))
amount_final = round(amount, 2)

print(f"Each person should pay: £{amount_final}")