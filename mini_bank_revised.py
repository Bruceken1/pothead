initial_balance = float(input("What is the current account balance: "))
monthly_deposits = float(input("How much will you deposit monthly: "))
interest_rate = float(input("What is the interest rate: "))
monthly_withdrawals = float(input("How much will you spend per month?: "))
total_months = int(input("How many months do you want to simulate: ")) 


def simulate(initial_balance, monthly_deposits, monthly_withdrawals, interest_rate, total_months):
    
    if initial_balance < 0 or monthly_deposits < 0 or monthly_withdrawals < 0 or interest_rate < 0 or total_months < 0 :
        return None, 0 , False
    balance = initial_balance
    months = 0
    bankrupt = False
    
    while months < total_months:
        
        balance += balance * (interest_rate / 12)        
        balance += monthly_deposits 
        balance -= monthly_withdrawals
        months += 1
        
        if balance < 0:
            bankrupt = True
            break
        
    return balance, months, bankrupt

balance, months_simulated,bankrupt = simulate(initial_balance, monthly_deposits, monthly_withdrawals, interest_rate, total_months)

if balance is None:
    print("Invalid input. Please check your numbers.")

else:
    print("Your account balance is ", balance)
    print("Number of months simulated is ", months_simulated)
    print("Bankrupt? ", "Yes" if bankrupt else "No")

      
        
    
            
        
    
        