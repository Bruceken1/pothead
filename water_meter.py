current_level = float(input("Enter the current water level to estimate usage days left: "))

usage_rate = float(input("What is your usage rate in litres per day: "))

def days_left(current_level, usage_rate):
    
    
    if usage_rate <= 0:
        return None, None
    
    if current_level < 0:
        return None, None
    
    days = 0
         
    while current_level >= usage_rate:
        current_level -= usage_rate
        days += 1
        
    return days, current_level

days, remaining = days_left(current_level, usage_rate)

if days is None:
    print("Invalid input. Usage rate must be greater than 0.")

else:
    print("You have ", days, " full days left with ", remaining, " litres of water remaining")

    




    

days = days_left(current_level, usage_rate)

print("You have ", days, " days of water left with ", current_level, " litres of water remaining." )

