# Program to create and display a dictionary of student details

student = {}

student["name"] = input("Enter name: ")
student["roll"] = int(input("Enter roll number: "))
student["age"] = int(input("Enter age: "))

print("\nStudent Details:")
for key in student:
    print(key, ":", student[key])

'''#output
Enter name: Aviral
Enter roll number: 43
Enter age: 23
Student Details:
name : Aviral
roll : 43
age : 23
'''