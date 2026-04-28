# Program: Find sum of first N natural numbers

n = int(input("Enter a positive integer: "))

total = 0
# Calculate sum using for loop
for i in range(1, n + 1):
    total += i

print(total)




        

#---------------------------------------
'''output
Enter a positive integer: 10
55
'''