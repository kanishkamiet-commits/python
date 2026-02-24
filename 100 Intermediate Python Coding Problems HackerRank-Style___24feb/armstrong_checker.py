# -------------------------------------------------
# Program: Check whether a number is Armstrong
# -------------------------------------------------

# Input with validation
while True:
    try:
        num = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Invalid input! Please enter an integer value.")

# Convert number to string
num_str = str(abs(num))
length = len(num_str)

# Calculate Armstrong sum without loop
armstrong_sum = sum(int(digit) ** length for digit in num_str)

# Check condition
if armstrong_sum == abs(num):
    print("The number is an Armstrong number.")
else:
    print("The number is NOT an Armstrong number.")










#---------------------------------------------------
'''output
Enter an integer: 153
The number is an Armstrong number.
#------------------------------------------------------------
Enter an integer: 123
The number is NOT an Armstrong number. 
'''  