# Program: Print all prime numbers between 1 and N

n = int(input("Enter a positive integer: "))

num = 2

while num <= n:
    i = 2
    is_prime = True

    while i * i <= num:
        if num % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(num)

    num += 1










#---------------------------------------
'''output
Enter a positive integer: 20
2
3
5
7
11
13
17
19
'''

