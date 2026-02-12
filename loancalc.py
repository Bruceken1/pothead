loan_amount = int(input("Please enter your loan amount: "))

annual_interest = float(input("What is your annual interest rate in decimals?: "))

monthly_payments = int(input("How much will you pay per month?: "))

def get_payment_period():
    
    month = 0
    current_balance = loan_amount
    
    if monthly_payments <= current_balance*annual_interest /12:
        print("Your monthly payment is too low - The loan will never be paid off.")
        return
    
    while current_balance > 0:
        current_balance += current_balance*annual_interest/12
        
        current_balance -= monthly_payments
        
        month += 1
    return month

period = get_payment_period()

print("It will take you ", period, " months to pay off your loan")

    
        