# -------------------------------------------------------
# Function to validate score (0 to 100)
# -------------------------------------------------------
def is_valid_score(value):
    try:
        score = float(value)
        if 0 <= score <= 100:
            return True
        else:
            return False
    except ValueError:
        return False


# -------------------------------------------------------
# Online Exam Result Processor
# -------------------------------------------------------
def exam_result_processor():

    data = input("Enter student scores (0-100) separated by space: ").split()

    scores = []

    # Validate scores
    for item in data:
        if is_valid_score(item):
            scores.append(float(item))
        else:
            print(f"Invalid score ignored: {item}")

    if len(scores) < 3:
        print("At least 3 valid scores required to remove lowest 2.")
        return

    print("\nOriginal Scores:", scores)

    # Remove lowest 2 scores
    scores.sort()
    removed_scores = scores[:2]
    scores = scores[2:]

    print("Removed Lowest 2 Scores:", removed_scores)

    # Add grace marks (5) to scores between 30 and 35
    for i in range(len(scores)):
        if 30 <= scores[i] <= 35:
            scores[i] += 5
            print(f"Grace added to student with original score between 30-35")

    # Count passed students (>= 40)
    passed_count = 0
    for score in scores:
        if score >= 40:
            passed_count += 1

    print("\nProcessed Scores:", scores)
    print("Number of Students Passed :", passed_count)


# Run Program
exam_result_processor()




'''output
Enter student scores (0-100) separated by space: 45 32 28 50 38 29
Original Scores: [45.0, 32.0, 28.0, 50.0, 38.0, 29.0]
Removed Lowest 2 Scores: [28.0, 29.0]
Grace added to student with original score between 30-35
Processed Scores: [45.0, 32.0, 50.0, 38.0]
Number of Students Passed (>= 40): 2
'''