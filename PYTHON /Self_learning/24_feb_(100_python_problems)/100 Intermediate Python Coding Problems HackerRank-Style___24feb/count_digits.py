# -------------------------------------------------
# Program: Count Digits in a Number
# -------------------------------------------------

# Input with validation
while True:
    try:
        num = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Invalid input! Please enter an integer value.")

# Convert number to string and count digits
digit_count = len(str(abs(num)))

print("Number of digits =", digit_count)









#---------------------------------------------------
'''output   
Enter an integer: 12345
Number of digits = 5
#------------------------------------------------------------
Enter an integer: -6789
Number of digits = 4
#------------------------------------------------------
'''