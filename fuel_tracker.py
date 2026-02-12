consumption = float(input("Enter your vehicles consumption per kilometre in litres: "))
fuel_present = int(input("Enter the remaining litres in your tank: "))


def distance_estimation(consumption, fuel_present):
    kilometres = 0
    
    while fuel_present > 0:
        fuel_present -= consumption
        kilometres += 1
    return kilometres

distance = distance_estimation(consumption, fuel_present)

print("Your fuel will last you ", distance, " kilometres before it runs out!")

    