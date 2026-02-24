# Program: Count Frequency of Elements in List

# Read input (space-separated numbers)
numbers = list(map(int, input().split()))

# Dictionary to store frequency
frequency = {}

# Count frequency
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# Print frequency of each element
for key in frequency:
    print(key, ":", frequency[key])









#----------------------------------------
'''output
Input:
1 2 2 3 3 3
Output:
1 : 1
2 : 2
3 : 3
'''
