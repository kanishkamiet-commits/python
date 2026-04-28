# -------------------------------------------------
# Program: Find GCD using while loop
# -------------------------------------------------

# Input with validation
while True:
    try:
        a = int(input("Enter first integer: "))
        b = int(input("Enter second integer: "))
        break
    except ValueError:
        print("Invalid input! Please enter integer values only.")

# Handle negative numbers
a = abs(a)
b = abs(b)

# Euclidean Algorithm using while loop
while b != 0:
    remainder = a % b
    a = b
    b = remainder

print("GCD is:", a)










#---------------------------------------
'''output
Enter first integer: 48
Enter second integer: 18
GCD is: 6
'''
