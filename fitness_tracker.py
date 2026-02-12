weekly_steps = int(input("Enter the number of steps you intend to achieve this week: "))

average_steps = int(input("Enter the average steps you walk per day: "))

def get_days2target(weekly_steps, average_steps):
    total_steps = 0
    days = 0
    
    while total_steps < weekly_steps:
        total_steps += average_steps
        days += 1
        
    return days

days_needed = get_days2target(weekly_steps, average_steps)

print("It will take you ", days_needed, " days to reach your target.")    
    
    

