# -------------------------------------------------
# Program: Generate Fibonacci Series using Function
# -------------------------------------------------

def fibonacci(n):
    a = 0
    b = 1
    
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


# Read input
num = int(input())

# Call function
fibonacci(num)









#----------------------------------------
'''output
Input:
10
Output:
0 1 1 2 3 5 8 13 21 34
'''