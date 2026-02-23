# Program to count vowels in a string

text = input("Enter a string: ")

count = 0  # Variable to count vowels

# Convert to lowercase for easy comparison
for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Total vowels:", count)

#-------------------------------------------------




'''#output
Enter a string: Hello world 123
Total vowels: 3
'''
