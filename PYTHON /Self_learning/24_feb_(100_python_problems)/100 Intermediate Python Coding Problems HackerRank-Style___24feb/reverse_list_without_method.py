# Program: Reverse a List Without Using reverse() Method

# Read input (space-separated numbers)
numbers = list(map(int, input().split()))

# Create empty list for reversed elements
reversed_list = []

# Traverse list in reverse order
for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

# Print reversed list
print(*reversed_list)








#----------------------------------------
'''output
Input:
1 2 3 4 5
Output:
5 4 3 2 1
'''