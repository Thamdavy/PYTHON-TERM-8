# Get the desired future value.
future_value = float(input('Enter the desired future value: '))

# Get the annual interest rate.
rate = float(input('Enter the annual interest rate (as a decimal, e.g., 0.05 for 5%): '))

# Get the number of years.
years = int(input('Enter the number of years the money will grow: '))

# Calculate the amount needed to deposit.
present_value = future_value / (1.0 + rate) ** years

# Display the amount needed to deposit.
print(f'You will need to deposit: ${present_value:.2f}')


