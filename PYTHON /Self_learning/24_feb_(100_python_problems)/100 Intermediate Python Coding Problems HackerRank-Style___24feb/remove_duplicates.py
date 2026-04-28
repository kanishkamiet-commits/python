# Program: Remove Duplicate Elements from List

# Read input (space-separated numbers)
numbers = list(map(int, input().split()))

# Create empty list for unique elements
unique_list = []

# Remove duplicates
for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

# Print result
print(*unique_list)










#----------------------------------------
'''output
Input:
1 2 3 2 4 1
Output:
1 2 3 4
'''