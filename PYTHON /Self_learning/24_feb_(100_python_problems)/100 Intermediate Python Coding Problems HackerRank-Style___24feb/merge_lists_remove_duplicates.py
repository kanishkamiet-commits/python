# Program: Merge Two Lists and Remove Duplicates

# Read first list (space-separated numbers)
list1 = list(map(int, input().split()))

# Read second list (space-separated numbers)
list2 = list(map(int, input().split()))

# Merge lists
merged_list = list1 + list2

# Remove duplicates while maintaining order
unique_list = []

for item in merged_list:
    if item not in unique_list:
        unique_list.append(item)

# Print result
print(*unique_list)









#----------------------------------------
'''output
Input:
1 2 3
2 4 5
Output:
1 2 3 4 5
'''
