# -------------------------------------------------
# Program: Calculate BMI Category
# -------------------------------------------------

# Input with validation
while True:
    try:
        weight = float(input("Enter weight in kilograms: "))
        height = float(input("Enter height in meters: "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter numeric values only.")

# BMI Calculation
bmi = weight / (height ** 2)

print("BMI =", round(bmi, 2))

# BMI Category
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")









#--------------------------------------------------------
'''output
Enter weight in kilograms: 70
Enter height in meters: 1.75
BMI = 22.86
Category: Normal weight.
#--------------------------------------------------------
Enter weight in kilograms: 50
Enter height in meters: 1.75
BMI = 16.33
Category: Underweight.
#--------------------------------------------------------
Enter weight in kilograms: 80
Enter height in meters: 1.75
BMI = 26.12
Category: Overweight.
#--------------------------------------------------------
Enter weight in kilograms: 95
Enter height in meters: 1.75
BMI = 31.02
Category: Obese.
#--------------------------------------------------------
'''
