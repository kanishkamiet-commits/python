# -------------------------------------------------
# Program: Check whether a character is
#          Digit or Alphabet
# -------------------------------------------------

# Input with validation
while True:
    ch = input("Enter a single character: ").strip()

    if len(ch) != 1:
        print("Please enter only one character.")
    else:
        break

# Check condition
if ch.isalpha():
    print("The character is an Alphabet.")
elif ch.isdigit():
    print("The character is a Digit.")
else:
    print("The character is neither a Digit nor an Alphabet.")







#--------------------------------------------------------
'''output
Enter a single character: a
The character is an Alphabet.
#-------------------------------------------
Enter a single character: 5
The character is a Digit.
#------------------------------------------------
Enter a single character: @
The character is neither a Digit nor an Alphabet.
'''