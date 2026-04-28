# -------------------------------------------------
# Program: Check whether a given year is a Leap Year
# -------------------------------------------------
# Input with validation
while True:
    try:
        year = int(input("Enter a year: "))
        if year <= 0:
            print("Please enter a positive year.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter a valid integer year.")

# Leap year logic
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year.")
else:
    print(year, "is not a Leap Year.")





# ------------------------------------------------
'''#output
Enter a year: 2020
2020 is a Leap Year.
#------------------------------------------------------
Enter a year: 1900
1900 is not a Leap Year.
'''
