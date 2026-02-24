# -------------------------------------------------
# Program: Generate Fibonacci Series using for loop
# -------------------------------------------------

# Input with validation
while True:
    try:
        n = int(input("Enter number of terms: "))
        
        # Check if number of terms is positive
        if n <= 0:
            print("Please enter a positive integer.")
            continue
        
        break
    except ValueError:
        print("Invalid input! Please enter an integer value.")

# Initialize first two terms
a = 0
b = 1

# Generate Fibonacci series
for i in range(n):
    print(a)
    
    # Update values
    next_term = a + b
    a = b
    b = next_term









  #----------------------------------------------------------------------
'''output
Enter number of terms: 10
0
1
1
2
3
5
8
13
21
34
'''
