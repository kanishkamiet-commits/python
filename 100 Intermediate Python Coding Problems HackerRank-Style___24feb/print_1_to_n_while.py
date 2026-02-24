# -------------------------------------------------
# Program: Print numbers from 1 to N
#          using while loop
# -------------------------------------------------

# Input with validation
while True:
    try:
        n = int(input("Enter a positive integer N: "))
        if n <= 0:
            print("Please enter a positive integer.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter an integer value.")

# Initialize counter
i = 1

# While loop
while i <= n:
    print(i)
    i += 1




#---------------------------------------------------
'''output
Enter a positive integer N: 5
1
2
5
3
4
Enter a positive integer N: -3
Please enter a positive integer.
Enter a positive integer N: abc
Invalid input! Please enter an integer value.
Enter a positive integer N: 3
'''