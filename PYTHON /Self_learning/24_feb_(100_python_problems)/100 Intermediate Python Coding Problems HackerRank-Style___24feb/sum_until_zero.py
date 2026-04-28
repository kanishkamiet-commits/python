# -------------------------------------------------
# Program: Accept numbers until 0 is entered
#          and print their sum
# -------------------------------------------------

total = 0

while True:
    try:
        num = float(input("Enter a number : "))
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        continue

    if num == 0:
        break

    total += num

print("Sum of entered numbers =", total)







#---------------------------------------
'''output
Enter a number : 5
Enter a number : 10
Enter a number : -3
Enter a number : 0
Sum of entered numbers = 12.0
'''