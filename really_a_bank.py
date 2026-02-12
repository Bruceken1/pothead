import random

initial_balance = float(input("What is your current balance? : "))
avg_deposit = float(input("What is your current salary: "))
avg_withdrawals = float(input("How much will you be spending monthly: "))
total_months = int(input("How many months do you want the sim to run: "))
interest_rate = float(input("What interest rate (in decimals) do you want to apply annualy: "))
var_factor = float(input("What var factor do you want to use (decimals): "))
safety_threshold = float(input("What is your safety threshold: "))
reduction_percent = float(input("What percentage of reduction do you expect after balance is below threshold? : "))

def sim(initial_balance, avg_deposit, avg_withdrawals, total_months,interest_rate, var_factor, safety_threshold, reduction_percent):
    
    if any(x < 0  for x in [initial_balance, avg_deposit, avg_withdrawals, total_months, interest_rate, var_factor,safety_threshold, reduction_percent]):
    
    
        return None, 0 , False, [], total_months
    
    balance = initial_balance
    months = 0
    bankrupt = False
    monthly_balances = []
    
    while months < total_months:
        
        balance += balance*(interest_rate/12)
        
        deposit = avg_deposit * random.uniform(1-var_factor, 1 + var_factor)
        
        withdrawals = avg_withdrawals * random.uniform(1 - var_factor, 1 + var_factor)
        
        
        if balance < safety_threshold:
            withdrawals *= (1 - reduction_percent)

        balance += deposit - withdrawals
        
        monthly_balances.append(balance)                    
            
        if balance < 0 :
            bankrupt = True
            months += 1
            break
        
        months += 1
        
    return balance, months, bankrupt, monthly_balances, total_months

balance, months, bankrupt, monthly_balances, total_months = sim(initial_balance, avg_deposit, avg_withdrawals, total_months, interest_rate, var_factor, safety_threshold, reduction_percent)

if balance is None:
    print("Invalid input. Check your figures.")

else:
    print("\nSimulation Results")
    print("-------------------")
    print("Your remaining balance is ", balance)
    print("\nThe number of months simulated is ", total_months)
    print("\nYou are bankrupt " if bankrupt else "You are not bankrupt")
    print("\nBelow is your monthly statement: ", [round(balances, 2) for balances in monthly_balances])
          