n=int(input("enter number of rows:"))

for i in range(1, n+1):
    print(" "*(n-i), end="")
    for j in range(1, i+1):
        print(i, end=" ")
    print()






'''output:
enter number of rows:5
    1 
   2 2 
  3 3 3 
 4 4 4 4    
5 5 5 5 5
'''
