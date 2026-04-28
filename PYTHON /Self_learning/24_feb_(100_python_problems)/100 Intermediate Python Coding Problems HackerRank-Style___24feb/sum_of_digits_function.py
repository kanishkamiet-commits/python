# -------------------------------------------------
# Program: Find Sum of Digits using Function
# -------------------------------------------------

def sum_of_digits(n):
    total = 0
    
    # Convert number to positive (handles negative input)
    n = abs(n)
    
    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
    
    return total


# Read input
num = int(input())

# Print result
print(sum_of_digits(num))









#----------------------------------------
'''output
Input:
1234
Output:
10
'''
