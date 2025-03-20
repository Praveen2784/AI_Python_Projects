def calculate_grade(score):
    """
    Calculates the grade based on the given score.

    Args:
        score (int): The student's score.

    Returns:
        str: The grade (A, B, C, D, or E).
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'E'

# Get the student's score with error handling
try:
    score = int(input("Enter the student's score: "))
    if 0 <= score <= 100:
        grade = calculate_grade(score)
        print(f"The grade is: {grade}")
    else:
        print("Error: Please enter a valid score between 0 and 100.")
except ValueError:
    print("Error: Please enter a valid numeric score.")
