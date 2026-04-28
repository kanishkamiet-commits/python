# -------------------------------------------------
# Program: Assign Grades Based on Marks
# -------------------------------------------------

# Input with validation
while True:
    try:
        marks = float(input("Enter marks: "))
        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter numeric value.")

# Grade assignment
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade =", grade)





# -------------------------------------------------
'''#output
Enter marks: 95
Grade = A+
#------------------------------------------------------
Enter marks: 56
Grade = D
#------------------------------------------------------
Enter marks: 37
Grade = F
#------------------------------------------------------
Enter marks: abc
Invalid input! Please enter numeric value.
'''