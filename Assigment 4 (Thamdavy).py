# Get the loan amount.
loan_amount = int(input("Please input the loan amount you borrowed: "))

# Get the annual interest rate.
i = float(input("Enter the annual interest rate (as a decimal, e.g., 0.05 for 5%): "))

# Get the number of years to repay the loan.
n = int(input("How many years to pay the loan: "))

# Convert annual interest rate to monthly and calculate number of months.
i = i / 12  # Monthly interest rate
n = n * 12  # Total number of months

# Calculate the monthly payment using the loan formula.
# Formula: M = P * (r * (1 + r)^n) / ((1 + r)^n - 1)
total_payment = loan_amount * (i * (1 + i) ** n) / ((1 + i) ** n - 1)

# Display the monthly payment amount.
print(f"The amount to pay every month is: ${total_payment:.2f}")
