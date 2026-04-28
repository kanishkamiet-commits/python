# -------------------------------------------------
# Program: Find Maximum of Three Numbers using Function
# -------------------------------------------------

def find_max(a, b, c):
    maximum = a
    
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c
    
    return maximum


# Read input
num1 = float(input())
num2 = float(input())
num3 = float(input())

# Print result
print(find_max(num1, num2, num3))





#---------------------------------------------- 
'''output
Input:
3
5
2
Output:
5.0
'''