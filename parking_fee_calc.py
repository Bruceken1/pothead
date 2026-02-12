hours_parked = float(input("Enter the number of hours you parked your car: "))

def parking_charge(hours_parked):
    
    if hours_parked > 24:
        return None
    if hours_parked > 10:
        return 25
    if hours_parked <= 2:
        return 2       
        
parking_fee = parking_charge(hours_parked)

print("Your total parking fee is $", parking_fee,)
        