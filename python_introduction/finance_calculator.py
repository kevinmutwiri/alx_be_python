income = input("Enter your monthly income: ")
expenses = input("Enter your total monthly expenses: ")

savings = float(income) - float(expenses)
projected_savings = savings * 12 + (savings * 12 * 0.05)

print(f"Your monthly savings are ${savings}.")
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")
