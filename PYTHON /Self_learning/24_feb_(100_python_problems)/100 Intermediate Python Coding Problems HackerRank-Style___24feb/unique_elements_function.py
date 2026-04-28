# -------------------------------------------------
# Program: Return Unique Elements from a List
#          using Function
# -------------------------------------------------

def get_unique_elements(lst):
    unique_list = []
    
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    
    return unique_list


# Read input
# Example input format: 1 2 3 2 4 1
numbers = list(map(int, input().split()))

# Call function and print result
result = get_unique_elements(numbers)
print(*result)








#----------------------------------------
'''output
Input:
1 2 3 2 4 1
Output:
1 2 3 4
'''
