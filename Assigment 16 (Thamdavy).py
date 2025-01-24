def amortization(loan, i, n):
    # Calculate monthly payment
    payment = loan * ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
    return payment

def show_payment(my_loan, my_i, my_n):
    # Adjust for monthly interest rate and total number of payments
    my_n = my_n * 12  # Convert years to months
    my_i = my_i / 12  # Convert annual rate to monthly rate
    
    my_payment = amortization(my_loan, my_i, my_n)
    y = 1  # Initialize month counter

    while y <= my_n:
        interest_paid = my_loan * my_i  # Calculate interest for the month
        principle_paid = my_payment - interest_paid  # Principal portion of payment
        my_loan = my_loan - principle_paid  # Remaining loan balance

        # Print details for the month
        print(f"Month {y}: Payment: {round(my_payment, 2)}, Interest: {round(interest_paid, 2)}, "
              f"Principal Paid: {round(principle_paid, 2)}, Remaining Loan: {round(my_loan, 2)}")
        print(".............>")
        
        y += 1  # Increment month counter

# Call the function to test
show_payment(30000, 0.03, 4)
