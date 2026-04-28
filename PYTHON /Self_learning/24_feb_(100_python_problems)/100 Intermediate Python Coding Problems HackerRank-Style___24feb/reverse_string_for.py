# -------------------------------------------------
# Program: Reverse a string using for loop
# -------------------------------------------------

# Input
s = input("Enter a string: ")

# Initialize empty string to store reversed result
reversed_string = ""

# Traverse string in reverse order using for loop
for i in range(len(s) - 1, -1, -1):
    reversed_string += s[i]

# Output
print(reversed_string)






 #----------------------------------------------------------------------
'''output
Enter a string: Hello, World!
!dlroW ,olleH
'''

