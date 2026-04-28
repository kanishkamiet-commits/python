# -------------------------------------------------
# Program: Determine the Type of Triangle
# -------------------------------------------------

# Input with validation
while True:
    try:
        a = float(input("Enter side 1: "))
        b = float(input("Enter side 2: "))
        c = float(input("Enter side 3: "))

        if a <= 0 or b <= 0 or c <= 0:
            print("Sides must be positive numbers.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter numeric values only.")

# Check if valid triangle (Triangle Inequality Theorem)
if a + b > c and a + c > b and b + c > a:

    # Determine type
    if a == b == c:
        print("The triangle is Equilateral.")
    elif a == b or b == c or a == c:
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")
else:
    print("The given sides do not form a valid triangle.")






#--------------------------------------------------------
'''output
Enter side 1: 3
Enter side 2: 3
Enter side 3: 3
The triangle is Equilateral.
#--------------------------------------------------------
Enter side 1: 4
Enter side 2: 4
Enter side 3: 5
The triangle is Isosceles.
#--------------------------------------------------------
Enter side 1: 3
Enter side 2: 4
Enter side 3: 5
The triangle is Scalene.
#--------------------------------------------------------
Enter side 1: 1
Enter side 2: 2
Enter side 3: 3
The given sides do not form a valid triangle.   
#--------------------------------------------------------
'''