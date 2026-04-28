# Program to check whether a key exists in dictionary
student = {}
#to insert an element
input("Enter name: ")
student['name'] = input("Enter name: ")
student['roll'] = int(input("Enter roll number: "))
student['age'] = int(input("Enter age: "))
# Check using 'in' operator
if "age" in student:
    print("Key 'age' exists in dictionary")
else:
    print("Key not found")




    '''#output
Enter name: abc
Enter roll number: 43
Enter age: 23
Key 'age' exists in dictionary
'''