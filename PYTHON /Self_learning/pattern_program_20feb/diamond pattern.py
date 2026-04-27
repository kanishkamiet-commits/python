n = 5

# Upper pyramid
for i in range(n):
    print(" "*(n-i-1) + "*"*(2*i+1))

# Lower inverted pyramid
for i in range(n-2, -1, -1):
    print(" "*(n-i-1) + "*"*(2*i+1))









'''Output:
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***  
    *
    '''