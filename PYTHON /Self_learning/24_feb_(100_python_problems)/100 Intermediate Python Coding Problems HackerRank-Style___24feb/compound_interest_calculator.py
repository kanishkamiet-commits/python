# -------------------------------------------------
# Program: Calculate Compound Interest
# -------------------------------------------------

def calculate_compound_interest():

    # Input with validation
    while True:
        try:
            principal = float(input("Enter Principal Amount: "))
            rate = float(input("Enter Rate of Interest: "))
            time = float(input("Enter Time (in years): "))
            break
        except ValueError:
            print("Invalid input! Please enter numeric values only.")

    # Check for negative values
    if principal < 0 or rate < 0 or time < 0:
        print("Values cannot be negative.")
        return

    # Compound Interest Formula
    amount = principal * (1 + rate / 100) ** time
    compound_interest = amount - principal

    print("Compound Interest =", compound_interest)
    print("Total Amount =", amount)


# Function call
calculate_compound_interest()




# -------------------------------------------------
'''#output
Enter Principal Amount: 1000
Enter Rate of Interest: 5
Enter Time (in years): 2
Compound Interest = 102.5
Total Amount = 1102.5
#------------------------------------------------------------
Enter Principal Amount: -1000
Enter Rate of Interest: 5
Enter Time (in years): 2
Values cannot be negative.
''' 