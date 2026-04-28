# -------------------------------------------------
# Program: Convert Celsius to Fahrenheit
# -------------------------------------------------

def convert_temperature():

    # Input with validation
    while True:
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            break
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

    # Conversion Formula
    fahrenheit = (celsius * 9/5) + 32

    print("Temperature in Fahrenheit =", fahrenheit)


# Function call
convert_temperature()







# -------------------------------------------------
'''#output
Enter temperature in Celsius: 25
Temperature in Fahrenheit = 77.0
#------------------------------------------------------------
Enter temperature in Celsius: abc
Invalid input! Please enter a numeric value.
#------------------------------------------------------------
Enter temperature in Celsius: -10
Temperature in Fahrenheit = 14.0
#-------------------------------------------------------
Enter temperature in Celsius: 0
Temperature in Fahrenheit = 32.0
'''