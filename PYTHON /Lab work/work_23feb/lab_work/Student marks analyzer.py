# Student Marks Analyzer with Validation

def get_marks():
    marks = []
    
    try:
        n = int(input("Enter number of students: "))
        if n <= 0:
            print("Number of students must be greater than 0.")
            return []
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        return []
    
    for i in range(n):
        while True:
            try:
                mark = float(input(f"Enter marks for student {i+1}: "))
                marks.append(mark)
                break
            except ValueError:
                print("Invalid input! Please enter numeric value.")
    
    return marks


def remove_invalid_marks(marks):
    valid_marks = []
    for mark in marks:
        if 0 <= mark <= 100:
            valid_marks.append(mark)
        else:
            print(f"Invalid mark removed: {mark}")
    return valid_marks


def calculate_average(marks):
    if len(marks) == 0:
        return 0
    return sum(marks) / len(marks)


def find_toppers(marks):
    if len(marks) == 0:
        return []
    highest = max(marks)
    toppers = [i+1 for i, mark in enumerate(marks) if mark == highest]
    return highest, toppers


def assign_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# Main Program
marks = get_marks()

if marks:
    print("\nOriginal Marks:", marks)
    
    valid_marks = remove_invalid_marks(marks)
    print("Valid Marks:", valid_marks)
    
    if valid_marks:
        avg = calculate_average(valid_marks)
        print("Average Marks:", round(avg, 2))
        
        highest, toppers = find_toppers(valid_marks)
        print("Highest Marks:", highest)
        print("Topper Student Number(s):", toppers)
        
        grade = assign_grade(avg)
        print("Grade Based on Average:", grade)
    else:
        print("No valid marks available to analyze.")
else:
    print("Program terminated due to invalid input.")








    ''''output:
Enter number of students: 5
Enter marks for student 1: 85
Enter marks for student 2: 92
Enter marks for student 3: 78
Enter marks for student 4: 105
Invalid mark removed: 105.0
Enter marks for student 5: 88
Original Marks: [85.0, 92.0, 78.0, 105.0, 88.0]
Valid Marks: [85.0, 92.0, 78.0, 88.0]
Average Marks: 85.75
Highest Marks: 92.0
Topper Student Number(s): [2]
Grade Based on Average: A
    '''
