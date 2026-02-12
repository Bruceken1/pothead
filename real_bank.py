import random

initial_balance = float(input("Enter your starting balance: "))
avg_deposit = float(input("Enter your average monthly deposit: "))
avg_withdrawal = float(input("Enter your average monthly expenditure: "))
interest_rate = float(input("Enter the annual interest rate: "))
total_months = int(input("Enter the number  of months to simulate: "))
var_factor = float(input("How much deposits/withdrawals can randomly vary (In decimals): "))

def sim(initial_balance, avg_deposit, avg_withdrawal, interest_rate, total_months):
    
    if initial_balance < 0 or avg_deposit < 0 or avg_withdrawal < 0 or interest_rate < 0 or total_months < 0:
        return None, 0 , False, []
    balance = initial_balance
    months = 0
    bankrupt = False
    monthly_balances = []
    
    while months < total_months:
        
        balance += balance*(interest_rate/12)
        
        deposit = avg_deposit * random.uniform(1 - var_factor, 1 + var_factor)
        
        withdrawal = avg_withdrawal * random.uniform(1 - var_factor, 1 + var_factor)
        
        balance += deposit - withdrawal
        
        monthly_balances.append(balance)        
        
        months += 1
        
        if balance < 0:
            bankrupt = True
            break
        
        
        
    return balance, total_months, bankrupt, monthly_balances
    
    
balance, total_months, bankrupt, monthly_balances = sim(initial_balance, avg_deposit, avg_withdrawal, interest_rate, total_months)  

if balance is None:
    print("Invalid input. Please check your numbers.") 
    
else:
    print("Your final balance is ", balance)
    print("The number of months simulated is ", total_months)
    print("Bankrupt? ", "Yes" if bankrupt else "No")
    print("Your statement is shown below: ", [round(b, 2) for b in monthly_balances]) 
      
        