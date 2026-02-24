# -------------------------------------------------
# Program: Calculate Power without using exponent operator
# -------------------------------------------------

# Input with validation
while True:
    try:
        base = float(input("Enter base: "))
        exponent = int(input("Enter exponent (non-negative integer): "))
        
        if exponent < 0:
            print("Please enter a non-negative exponent.")
            continue
        
        break
    except ValueError:
        print("Invalid input! Please enter numeric values correctly.")

# Calculate power using loop
result = 1

for i in range(exponent):
    result *= base

# Output
print(result)







'''output
Enter base: 2
Enter exponent (non-negative integer): 5
32.0
'''