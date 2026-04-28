# -------------------------------------------------
# Program: Swap two numbers without using
#          a third variable 
# -------------------------------------------------

def swap_numbers():

    # Input with validation
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input! Please enter numeric values only.")
   
    # Swapping without third variable
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2

    print("\nAfter Swapping:")
    print("First Number =", num1)
    print("Second Number =", num2)


# Function call
swap_numbers()







# -------------------------------------------------
'''#output
Enter first number: 5
Enter second number: 10
After Swapping:
First Number = 10.0
Second Number = 5.0
''' 