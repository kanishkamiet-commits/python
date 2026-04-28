# -------------------------------------------------
# Program: Check Palindrome String using Function
# -------------------------------------------------

def is_palindrome(s):
    return s == s[::-1]


# Read input
text = input()

# Check and print result
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")




 #----------------------------------------------
'''output
Enter a string: madam
Palindrome
#----------------------------------------------
Enter a string: hello
Not Palindrome
'''   