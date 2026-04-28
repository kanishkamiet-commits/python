# -------------------------------------------------
# Program: Count Vowels using Function
# -------------------------------------------------

def count_vowels(s):
    count = 0
    for ch in s:
        if ch in "aeiouAEIOU":
            count += 1
    return count


# Read input
text = input()

# Print result
print(count_vowels(text))









#----------------------------------------
'''output
Input:
Hello World
Output:
3
'''