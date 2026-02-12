starting_salary = float(input("Enter your starting salary: "))
    
portion_2_b_saved = float(input("Enter the percentage you wish to save in decimals: "))
    
total_cost = float(input("Enter the total cost of your dream home: "))


def months_to_save():
    
    portion_down_payment = 0.25
    
    down_payment = total_cost * portion_down_payment
    
    current_savings = 0
    
    rS = 0.04
    
    month = 0
    
    while current_savings < down_payment:
        monthly_return = current_savings * rS/12
        
        monthly_salary_saving = starting_salary/12 * portion_2_b_saved
        
        current_savings += monthly_return + monthly_salary_saving
        
        month += 1
        
    return month
    
    

period = months_to_save()
     
print("It will take you ",period, " months to afford your dream home.")
