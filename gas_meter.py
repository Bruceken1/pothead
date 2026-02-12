current_quantity = float(input("Enter the amount of gas remaining in Kgs: "))
usage = float(input("Enter the amount of gas you use per day to cook in Kgs: "))


def days_remaining(current_quantity, usage):
    
    # Validate input
    if usage <= 0:
        return None, None
    
    if current_quantity < 0:
        return None, None
    
    days = 0

    # Simulate day-by-day usage
    while current_quantity >= usage:
        current_quantity -= usage
        days += 1
        
    return days, current_quantity


# Call function ONCE and unpack properly
days, remaining = days_remaining(current_quantity, usage)

# Handle output cleanly
if days is None:
    print("Invalid input. Usage must be greater than 0 and gas cannot be negative.")
else:
    print("You have", days, "full days of cooking gas left.")
    print("Remaining gas after that:", round(remaining, 2), "Kgs")
