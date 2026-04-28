# Program: Separate Even and Odd Numbers from List

# Read input (space-separated numbers)
numbers = list(map(int, input().split()))

even = []
odd = []

# Separate numbers
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

# Print results
print("Even numbers:")
print(*even)

print("Odd numbers:")
print(*odd)








#----------------------------------------
'''output
Input:
1 2 3 4 5 6
Output:
Even numbers:
2 4 6
Odd numbers:
1 3 5
'''
