def get_cuberoot(cube):
    if cube == 0:
        return 0
    if cube > 0:
        start = 0
        end = cube
        step = 1
    else:
        start = cube
        end = 0
        step = 1
        
    for guess in range(start, end+1, step):
        if guess**3 == cube:
            return guess

number = int(input("Enter a number to get the cube root: "))
result = get_cuberoot(number)
print("The cube root of", number, "is", result)