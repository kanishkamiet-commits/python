# Program: Find Smallest Element in a List

# Read input (space-separated numbers)
numbers = list(map(int, input().split()))

# Assume first element is smallest
smallest = numbers[0]

# Find smallest element
for num in numbers:
    if num < smallest:
        smallest = num

# Print result
print(smallest)







#----------------------------------------
'''output
Input:
5 3 8 1 4
Output:
1
'''
