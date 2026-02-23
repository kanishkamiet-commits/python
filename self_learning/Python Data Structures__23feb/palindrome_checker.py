# Program to check if a string is palindrome

text = input("Enter a string: ")

# Compare original string with reversed string
if text == text[::-1]:
    print("The string is Palindrome")
else:
    print("The string is Not Palindrome")



#-------------------------------------------------

'''#output
Enter a string: abcdcba
The string is Palindrome
'''

#-------------------------------------------------
'''#output
Enter a string: hello
The string is Not Palindrome
'''
