# -------------------------------------------------
# Program: Find the Greatest of Four Numbers
# -------------------------------------------------

# Input with validation
while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        num4 = float(input("Enter fourth number: "))
        break
    except ValueError:
        print("Invalid input! Please enter numeric values only.")

# Finding greatest number
greatest = num1

if num2 > greatest:
    greatest = num2
if num3 > greatest:
    greatest = num3
if num4 > greatest:
    greatest = num4

print("The greatest number is:", greatest)







#------------------------------------------------------
'''output
Enter first number: 5
Enter second number: 10
Enter third number: 3
Enter fourth number: 8
The greatest number is: 10.0
#------------------------------------------------------
Enter first number: -2
Enter second number: -5
Enter third number: -1
Enter fourth number: -3
The greatest number is: -1.0
#------------------------------------------------------
'''