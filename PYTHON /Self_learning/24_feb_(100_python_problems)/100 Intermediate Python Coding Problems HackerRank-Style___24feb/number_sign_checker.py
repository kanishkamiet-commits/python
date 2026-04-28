# -------------------------------------------------
# Program: Check whether a number is
#          Positive, Negative, or Zero
#          (with input validation)
# -------------------------------------------------

def check_number_sign():

    # Input with validation
    while True:
        try:
            num = float(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

    # Checking condition
    if num > 0:
        print("The number is Positive.")
    elif num < 0:
        print("The number is Negative.")
    else:
        print("The number is Zero.")


# Function call
check_number_sign()








# -------------------------------------------------
'''#output
Enter a number: -5
The number is Negative.
Enter a number: 0
The number is Zero.
Enter a number: 10
The number is Positive.
Enter a number: abc
Invalid input! Please enter a numeric value.
Enter a number: 3.14
The number is Positive.
'''