import random

initial_balance = float(input("What is your current balance? : "))
avg_deposit = float(input("What is your current salary: "))
avg_withdrawals = float(input("How much will you be spending monthly: "))
total_months = int(input("How many months do you want the sim to run: "))
interest_rate = float(input("What interest rate do you want to apply annualy: "))
var_factor = float(input("What var factor do you want to use (decimals): "))
safety_threshold = float(input("What is your safety threshold: "))
reduction_percent = float(input("What percentage of reduction do you expect after balance is below threshold? : "))

def sim(initial_balance, avg_deposit, avg_withdrawals, total_months,interest_rate):
    
    if initial_balance < 0 or avg_deposit < 0 or avg_withdrawals < 0 or interest_rate < 0 :
        return None, 0 , False, []
    
    balance = initial_balance
    months = 0
    bankrupt = False
    monthly_balances = []
    
    while months < total_months:
        
        balance += balance*(interest_rate/12)
        
        balance += avg_deposit * random.uniform(1-var_factor, 1 + var_factor)
        
        balance +- avg_withdrawals * random.uniform(1 - var_factor, 1 + var_factor)
        
        monthly_balances.append(balance)
        
        if balance < safety_threshold:
            new_avg_withdrawals = avg_withdrawals - (avg_withdrawals * reduction_percent)
            
            balance +- new_avg_withdrawals
            
        if balance < 0 :
            bankrupt = True
            break
        
        months += 1
        
    return balance, months, bankrupt, monthly_balances, total_months

balance, months, bankrupt, monthly_balances, total_months = sim(initial_balance, avg_deposit, avg_withdrawals, total_months, interest_rate)

if balance is None:
    print("Invalid input. Check your figures.")

else:
    print("Your remaining balance is ", balance)
    print("The number of months simulated is ", total_months)
    print("You are bankrupt " if bankrupt else "You are not bankrupt")
    print("Below is your monthly statement: ", [round(b, 2) for b in monthly_balances])
          