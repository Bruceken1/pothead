initial_balance = float(input("What is the current account balance: "))
monthly_deposits = float(input("How much will you deposit monthly: "))
interest_rate = float(input("What is the interest rate: "))
monthly_withdrawals = float(input("How much will you spend per month?: "))
total_months = float(input("How many months do you want to simulate: ")) 


def simulate(initial_balance, monthly_deposits, monthly_withdrawals, interest_rate, total_months):
    
    months = 0
    bankrupt = False
    while months < total_months:
        
        if initial_balance <= 0:
            return None
        if monthly_deposits <=0:
            return None
        if monthly_withdrawals < 0:
            return None
        if interest_rate < 0:
            return None
        
        initial_balance += interest_rate/12*initial_balance
        
        initial_balance += monthly_deposits
        
        initial_balance -= monthly_withdrawals
        
        
        months += 1
        
        if initial_balance < 0:
            bankrupt = True
            break
        
    return initial_balance, total_months, bankrupt

initial_balance, total_months = simulate(initial_balance, total_months)
 
print("Your account balance is $", initial_balance, " and the total number of months simulated was ", total_months) 

      
        
    
            
        
    
        