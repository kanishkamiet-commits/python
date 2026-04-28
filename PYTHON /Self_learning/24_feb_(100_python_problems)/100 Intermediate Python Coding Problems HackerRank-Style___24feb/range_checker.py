# -------------------------------------------------
# Program: Check whether a number lies
#          within a given range
# -------------------------------------------------

# Input with validation
while True:
    try:
        num = float(input("Enter the number: "))
        lower = float(input("Enter lower limit: "))
        upper = float(input("Enter upper limit: "))

        if lower > upper:
            print("Lower limit cannot be greater than upper limit.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter numeric values only.")

# Check range (inclusive)
if lower <= num <= upper:
    print("The number lies within the given range.")
else:
    print("The number does NOT lie within the given range.")









#------------------------------------------------------
'''output
Enter the number: 5
Enter lower limit: 1
Enter upper limit: 10
The number lies within the given range.
#------------------------------------------------------
Enter the number: 0
Enter lower limit: 1
Enter upper limit: 10
The number does NOT lie within the given range.
#------------------------------------------------------
'''