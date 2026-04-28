# -------------------------------------------------
# Program: Print Multiplication Table using while loop
# -------------------------------------------------

# Input with validation
while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input! Please enter an integer value.")

# Initialize counter
i = 1

# While loop to print table (1 to 10)
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1




    

#---------------------------------------------------
'''output
Enter a number: 7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
#------------------------------------------------------
Enter a number: abc
Invalid input! Please enter an integer value.
#------------------------------------------------------
'''