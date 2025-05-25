monthly_income = input("Enter your monthly income: ")
monthly_expense = input("Enter your total monthly expenses: ")

monthly_saving = float(monthly_income) - float(monthly_expense)
projected_saving = monthly_saving * 12 + (monthly_saving * 12 * 0.05)

print(f"Your monthly savings are ${monthly_saving}.")
print(f"Projected savings after one year, with interest, is: ${int(projected_saving)}.")
