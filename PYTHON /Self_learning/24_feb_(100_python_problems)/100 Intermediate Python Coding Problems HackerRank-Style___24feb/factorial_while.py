# -------------------------------------------------
# Program: Find Factorial using while loop
# -------------------------------------------------

# Input with validation
while True:
    try:
        n = int(input("Enter a non-negative integer: "))
        if n < 0:
            print("Factorial is not defined for negative numbers.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter an integer value.")

# Initialize variables
fact = 1
i = 1

# While loop to calculate factorial
while i <= n:
    fact *= i
    i += 1

print("Factorial of", n, "is:", fact)










#---------------------------------------------------
'''output
Enter a non-negative integer: 5
Factorial of 5 is: 120
#------------------------------------------------------------
Enter a non-negative integer: -3
Factorial is not defined for negative numbers.
#------------------------------------------------------
Enter a non-negative integer: abc
Invalid input! Please enter an integer value.
#---------------------------------------------------------
'''