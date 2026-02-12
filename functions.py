def is_even_with_return(i):
    """
    Docstring for is_even_with_return
    
    input: i, a positive int
    returns True if i is even, otherwise false
    """

    print('With return')
    remainder = i%2
    return remainder == 0

is_even_with_return(3)
print(is_even_with_return(3))

def is_even_with_return (i):
    """
    input : i, a positive int
    Does not return anything

    """
    print('Without Return')
    remainder = i%2