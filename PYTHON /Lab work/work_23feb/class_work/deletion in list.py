#create alist of 5 numbers and repeated numbers
numbers = [45, 23, 67, 45, 89, 23, 12,  34, 56]
#displaying the list
print("numbers are:")
print(numbers)
print("_____________________________")
#to delete the element from index 5
numbers.pop(5)
print("after deleting the element at index 5:")
print(numbers)
numbers.pop()
print("after deleting last element from list :")
print(numbers)
#to delete the element 45 from list
numbers.remove(45)
print("after deleting the element 45 from list:")
print(numbers)





'''Output:
numbers are:
[45, 23, 67, 45, 89, 23, 12, 34, 56]
_____________________________
after deleting the element at index 5:
[45, 23, 67, 45, 89, 12, 34, 56]
after deleting last element from list :
[45, 23, 67, 45, 89, 12, 34]
after deleting the element 45 from list:
[23, 67, 45, 89, 12, 34]
'''
