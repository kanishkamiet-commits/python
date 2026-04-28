# Program: Find Second Largest Number in a List
# (Without using max() or set())

# Read input (space-separated numbers)
numbers = list(map(int, input().split()))

# Check if list has at least two elements
if len(numbers) < 2:
    print("Second largest element does not exist.")
else:
    # Initialize largest and second largest
    largest = numbers[0]
    second_largest = numbers[0]

    # Find largest first
    for num in numbers:
        if num > largest:
            largest = num

    # Find second largest
    for num in numbers:
        if num != largest:
            if second_largest == largest or num > second_largest:
                second_largest = num

    # Check if second largest exists
    if second_largest == largest:
        print("Second largest element does not exist.")
    else:
        print(second_largest)












#----------------------------------------
'''output
Input:
1 2 3 4 5
Output:
4
'''
