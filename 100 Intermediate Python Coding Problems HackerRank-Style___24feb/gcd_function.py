# -------------------------------------------------
# Program: Find GCD using Function
# -------------------------------------------------

def find_gcd(a, b):
    # Make numbers positive
    a = abs(a)
    b = abs(b)
    
    # Euclidean Algorithm
    while b != 0:
        a, b = b, a % b
    
    return a


# Read input
num1 = int(input())
num2 = int(input())

# Print result
print(find_gcd(num1, num2))





#----------------------------------------
'''output
Input:
48
18
Output:
6
'''
