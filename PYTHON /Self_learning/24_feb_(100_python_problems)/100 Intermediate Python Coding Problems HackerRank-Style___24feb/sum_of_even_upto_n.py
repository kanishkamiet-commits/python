# -------------------------------------------------
# Program: Find Sum of Even Numbers up to N
# -------------------------------------------------

# Input with validation
while True:
    try:
        n = int(input("Enter a positive integer N: "))
        if n <= 0:
            print("Please enter a positive integer.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter an integer value.")

# Initialize variables
i = 2
total = 0

# While loop to add even numbers
while i <= n:
    total += i
    i += 2

print("Sum of even numbers up to", n, "is:", total)











#---------------------------------------------------
'''output
Enter a positive integer N: 10
Sum of even numbers up to 10 is: 30
#------------------------------------------------------------
Enter a positive integer N: -3
Please enter a positive integer.
#------------------------------------------------------
Enter a positive integer N: abc
Invalid input! Please enter an integer value.
'''


