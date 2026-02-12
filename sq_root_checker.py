def get_squareroot(square):
    if square < 0:
        return None
    if square == 0:
        return 0
    for guess in range(square+1):
        if guess**2 == square:
            return guess
       
number = int(input("Enters a number to get the square root: "))
result = get_squareroot(number)

print("The square root of ", number, " is ", result)