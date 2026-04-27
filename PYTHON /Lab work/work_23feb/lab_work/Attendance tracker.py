# -------------------------------------------------------
# Function to validate attendance input (only 0 or 1)
# -------------------------------------------------------
def is_valid_attendance(value):
    if value == "0" or value == "1":
        return True
    return False


# -------------------------------------------------------
# Attendance Tracker System
# -------------------------------------------------------
def attendance_tracker():

    data = input("Enter attendance (1 for Present, 0 for Absent) separated by space: ").split()

    attendance = []

    # Validate input
    for item in data:
        if is_valid_attendance(item):
            attendance.append(int(item))
        else:
            print(f"Invalid value ignored: {item}")

    # If no valid data
    if len(attendance) == 0:
        print("No valid attendance data entered.")
        return

    total_days = len(attendance)
    present_days = 0

    # Count present days
    for day in attendance:
        if day == 1:
            present_days += 1

    # Calculate percentage
    percentage = (present_days / total_days) * 100

    print("\nTotal Days:", total_days)
    print("Present Days:", present_days)
    print(f"Attendance Percentage: {percentage:.2f}%")

    # Check if below 75%
    if percentage < 75:
        print("Status: Below 75% - Short Attendance")
    else:
        print("Status: Good Attendance")

    # Replace consecutive absences with warning flag
    flagged_attendance = attendance.copy()

    for i in range(1, len(attendance)):
        if attendance[i] == 0 and attendance[i-1] == 0:
            flagged_attendance[i] = "W"

    print("Attendance with Warning Flags:", flagged_attendance)


# Run Program
attendance_tracker()




'''output :
Enter attendance (1 for Present, 0 for Absent) separated by space: 1 0 1 1 0 0 1
Total Days: 7
Present Days: 4
Attendance Percentage: 57.14%
Status: Below 75% - Short Attendance
Attendance with Warning Flags: [1, 0, 1, 1, 'W', 0, 1]
'''
