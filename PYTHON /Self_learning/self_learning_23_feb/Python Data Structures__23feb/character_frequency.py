# Program to count frequency of each character in a string

text = input("Enter a string: ")

freq = {}  # Empty dictionary

# Traverse each character
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Character frequency:", freq)

#-------------------------------------------------
'''#output
Enter a string: Hello 123
Character frequency: {'H': 1, 'e': 1, 'l': 2, 'o': 1, ' ': 1, '1': 1, '2': 1, '3': 1}
'''