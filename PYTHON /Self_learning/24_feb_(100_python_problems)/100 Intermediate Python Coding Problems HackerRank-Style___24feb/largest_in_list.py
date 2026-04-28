# Program: Find Largest Element in a List

# Read input (space-separated numbers)
numbers = list(map(int, input().split()))

# Assume first element is largest
largest = numbers[0]

# Find largest element
for num in numbers:
    if num > largest:
        largest = num

# Print result
print(largest)





#----------------------------------------
'''output
Input:
1 2 3 4 5
Output:
5
'''
