# Program: Find factorial using for loop

n = int(input("Enter a positive integer: "))
#---------------------------------------
fact = 1
# Calculate factorial using for loop
for i in range(1, n + 1):
    fact *= i
#---------------------------------------
print(fact)








#---------------------------------------
'''output
Enter a positive integer: 6
720
'''