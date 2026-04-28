# -------------------------------------------------
# Program: Reverse a Given Number
# -------------------------------------------------
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

# Reverse logic
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

reversed_num *= sign
print("Reversed Number =", reversed_num)






# -------------------------------------------------
'''#output
Enter an integer: 1234
Reversed Number = 4321
#------------------------------------------------------
Enter an integer: -5678
Reversed Number = -8765
'''