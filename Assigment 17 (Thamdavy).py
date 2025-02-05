def amortization(loan, i, n):
    payment = loan * ((i * (1 + i)**n) / ((1 + i)**n - 1))
    return payment

def show_payment(my_loan, my_i, my_n):
    my_i = my_i / 12  # Convert annual interest rate to monthly
    my_n = my_n * 12  # Convert years to months
    my_payment = amortization(my_loan, my_i, my_n)
    y = 1
    while y <= my_n:  # Changed < to <= to include the last month
        interest_paid = my_loan * my_i
        principle_paid = my_payment - interest_paid
        my_loan = my_loan - principle_paid
        print(f"({y}). Monthly payment {round(my_payment, 2)} Repayment {round(interest_paid, 2)} Loan payment {principle_paid:,.2f}")
        print(f"Old Borrow {my_loan:,.2f}")
        print("--------------------") # improved separator
        y = y + 1

loan_amount = float(input("Amount Loan "))  # added space for better user experience
interest = float(input("Interest rate "))       # added space
year = float(input("Date Payment "))      # added space

show_payment(loan_amount, interest, year)