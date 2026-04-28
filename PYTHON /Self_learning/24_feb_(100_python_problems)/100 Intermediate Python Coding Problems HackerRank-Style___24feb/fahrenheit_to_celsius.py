# -------------------------------------------------
# Program: Convert Fahrenheit to Celsius
# -------------------------------------------------

def convert_temperature():

    # Input with validation
    while True:
        try:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            break
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

    # Optional: Check for extremely low value (physical limit)
    if fahrenheit < -459.67:
        print("Temperature cannot be below absolute zero (-459.67°F).")
        return

    # Conversion Formula
    celsius = (fahrenheit - 32) * 5 / 9

    print("Temperature in Celsius =", celsius)


# Function call
convert_temperature()


# -------------------------------------------------
'''#output
Enter temperature in Fahrenheit: 77
Temperature in Celsius = 25.0


#------------------------------------------------------------
Enter temperature in Fahrenheit: abc
Invalid input! Please enter a numeric value.
'''