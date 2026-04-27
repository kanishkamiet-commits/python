n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    for j in range(i, 0, -1):
        print(j, end="")
    print()








'''output:  
enter number of rows:6
11
121
12321
1234321
123454321
12345654321
'''