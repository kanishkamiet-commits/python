# Program: Sort a List Without Using sort() Method

# Read input (space-separated numbers)
numbers = list(map(int, input().split()))

# Bubble Sort Algorithm
n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            # Swap elements
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Print sorted list
print(*numbers)












#----------------------------------------
'''output
Input:
5 3 8 1 4
Output:
1 3 4 5 8
'''