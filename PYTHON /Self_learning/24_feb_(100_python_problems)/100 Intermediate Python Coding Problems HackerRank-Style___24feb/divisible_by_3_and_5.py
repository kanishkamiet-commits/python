# -------------------------------------------------
# Program: Check whether a number is divisible
#          by both 3 and 5
# -------------------------------------------------

# Input with validation
while True:
    try:
        num = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Invalid input! Please enter an integer value.")

# Check divisibility
if num % 3 == 0 and num % 5 == 0:
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is NOT divisible by both 3 and 5.")









#--------------------------------------------------------           
'''output
Enter an integer: 15
The number is divisible by both 3 and 5.
#--------------------------------------------------------
Enter an integer: 10
The number is NOT divisible by both 3 and 5.
#--------------------------------------------------------
'''