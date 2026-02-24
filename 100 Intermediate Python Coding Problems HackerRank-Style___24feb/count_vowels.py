# Program: Count vowels in a string

s = input("Enter a string: ")

count = 0
# Count vowels in the string
for ch in s:
    if ch in "aeiouAEIOU":
        count += 1

print(count)







#---------------------------------------
'''output
Enter a string: Hello World
3
'''