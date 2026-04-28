# Program: Find Second Largest Number in a List

# Read input (space-separated numbers)
numbers = list(map(int, input().split()))

# Remove duplicates to handle correct second largest
unique_numbers = list(set(numbers))

# Check if at least two unique elements exist
if len(unique_numbers) < 2:
    print("Second largest element does not exist.")
else:
    # Find largest
    largest = max(unique_numbers)
    
    # Remove largest and find second largest
    unique_numbers.remove(largest)
    second_largest = max(unique_numbers)
    
    print(second_largest)










#----------------------------------------
'''output
Input:
1 2 3 4 5
Output:
4
'''
