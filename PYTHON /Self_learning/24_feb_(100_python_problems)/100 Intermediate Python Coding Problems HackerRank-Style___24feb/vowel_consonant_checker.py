# -------------------------------------------------
# Program: Check whether a character is
#          Vowel or Consonant
# -------------------------------------------------

# Input with validation
while True:
    ch = input("Enter a single alphabet character: ").strip()
    
    if len(ch) != 1:
        print("Please enter only one character.")
    elif not ch.isalpha():
        print("Please enter a valid alphabet letter (A-Z or a-z).")
    else:
        break

# Convert to lowercase for easy checking
ch = ch.lower()

# Check vowel or consonant
if ch in ['a', 'e', 'i', 'o', 'u']:
    print("The character is a Vowel.")
else:
    print("The character is a Consonant.")








#--------------------------------------------------------
'''output
Enter a single alphabet character: a
The character is a Vowel.
Enter a single alphabet character: b
The character is a Consonant.
'''
