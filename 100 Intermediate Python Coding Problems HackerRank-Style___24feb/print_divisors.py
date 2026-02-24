# -------------------------------------------------
# Program: Print all divisors of a number
# -------------------------------------------------

# Input with validation
while True:
    try:
        num = int(input("Enter a positive integer: "))
        
        # Check if number is positive
        if num <= 0:
            print("Please enter a positive integer.")
            continue
        
        break
    except ValueError:
        print("Invalid input! Please enter an integer value.")

# Loop from 1 to num to find divisors
for i in range(1, num + 1):
    
    # If remainder is 0, then i is a divisor
    if num % i == 0:
        print(i)






 #----------------------------------------------------------------------    
'''output
Enter a positive integer: 12
1
2
3
4
6
12
'''       