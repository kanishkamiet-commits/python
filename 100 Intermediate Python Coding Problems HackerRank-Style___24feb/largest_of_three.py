# -------------------------------------------------
# Program: Find the Largest of Three Numbers
# -------------------------------------------------

def find_largest():

    # Input with validation
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            num3 = float(input("Enter third number: "))
            break
        except ValueError:
            print("Invalid input! Please enter numeric values only.")

    # Finding largest
    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3

    print("The largest number is:", largest)


# Function call
find_largest()










# -------------------------------------------------
'''#output
Enter first number: 5
Enter second number: 10
Enter third number: 3
The largest number is: 10.0
Enter first number: -5
Enter second number: -10
Enter third number: -3
The largest number is: -3.0
Enter first number: 7
Enter second number: 7
Enter third number: 7
The largest number is: 7.0
Enter first number: abc
Invalid input! Please enter numeric values only.
Enter first number: 3.14
Enter second number: 2.71
Enter third number: 1.41
The largest number is: 3.14
''' 