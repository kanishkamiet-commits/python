# -------------------------------------------------
# Program: Find the Sum of Digits of a Number
#          (with input validation)
# -------------------------------------------------
 # Input enter an integer
num = int(input("Enter an integer: "))
     
    # Handle negative numbers
num = abs(num)

total = 0

    # Calculate sum of digits
while num > 0:
        digit = num % 10
        total += digit
        num = num // 10

print("Sum of digits =", total)







# -------------------------------------------------
'''#output
Enter an integer: 786
Sum of digits = 21
#------------------------------------------------------
Enter an integer: 2345
Sum of digits = 14
#------------------------------------------------------
'''