# -------------------------------------------------
# Program: Check Prime Number using Function
# -------------------------------------------------

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True


# Read input
num = int(input())

# Check and print result
if is_prime(num):
    print("Prime")
else:
    print("Not Prime")




 #----------------------------------------------------------------------
'''output
Input: 7
Prime
#----------------------------------------------------------------------
Input: 10
Not Prime
'''
