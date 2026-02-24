# -------------------------------------------------
# Program: Reverse a Number using while loop
# -------------------------------------------------

# Input with validation
while True:
    try:
        num = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Invalid input! Please enter an integer value.")

# Store original sign
sign = -1 if num < 0 else 1
num = abs(num)

reversed_num = 0

# While loop to reverse number
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

reversed_num *= sign

print("Reversed number =", reversed_num)











#---------------------------------------------------
'''output
Enter an integer: 12345
Reversed number = 54321
#------------------------------------------------------------
Enter an integer: -6789
Reversed number = -9876
#------------------------------------------------------
'''