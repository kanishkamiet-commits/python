# -------------------------------------------------
# Program: Calculate Simple Interest
# -------------------------------------------------

def calculate_simple_interest():

    # Input with validation
    while True:
        try:
            principal = float(input("Enter Principal Amount: "))
            rate = float(input("Enter Rate of Interest: "))
            time = float(input("Enter Time (in years): "))
            break
        except ValueError:
            print("Invalid input! Please enter numeric values only.")

    # Validation for negative values
    if principal < 0 or rate < 0 or time < 0:
        print("Values cannot be negative.")
        return

    # Simple Interest Formula
    simple_interest = (principal * rate * time) / 100

    print("Simple Interest =", simple_interest)


# Function call
calculate_simple_interest()





#-------------------------------------------------
'''#output
Enter Principal Amount: 1000
Enter Rate of Interest: 5
Enter Time (in years): 2
Simple Interest = 100.0
Enter Principal Amount: 500 
Enter Rate of Interest: 7.5 
#-------------------------------------------
Enter Time (in years): 3
Simple Interest = 112.5
Enter Principal Amount: -1000
Enter Rate of Interest: 5
Enter Time (in years): 2
Values cannot be negative.
'''
