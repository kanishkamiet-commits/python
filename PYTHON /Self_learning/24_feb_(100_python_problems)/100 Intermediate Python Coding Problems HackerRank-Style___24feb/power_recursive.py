# -------------------------------------------------
# Program: Calculate Power using Recursive Function
# -------------------------------------------------

def power(base, exponent):
    # Base case
    if exponent == 0:
        return 1
    
    # Recursive case
    return base * power(base, exponent - 1)


# Read input
base = float(input())
exponent = int(input())

# Print result
print(power(base, exponent))



#----------------------------------------
'''output
Input:
2
3
Output:
8.0
'''
