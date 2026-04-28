n=int(input("enter number of rows:"))
ch = 65
for i in range(1, n+1):
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()







'''output:
enter number of rows:7
A
B C
D E F   
G H I J
K L M N O
P Q R S T U
V W X Y Z [
''' 