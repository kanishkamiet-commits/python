n = int(input("enter number of rows:"))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(i*j, end=" ")
    print()










    '''output:
enter number of rows:9
1 2
2 4 6
3 6 9 12
4 8 12 16 20
5 10 15 20 25 30
6 12 18 24 30 36 42
7 14 21 28 35 42 49 56
8 16 24 32 40 48 56 64 72
9 18 27 36 45 54 63 72 81 90
'''
