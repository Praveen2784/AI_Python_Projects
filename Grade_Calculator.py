def calculate_grade(score):
  """
  Calculates the grade based on the given score.

  Args:
    score: The student's score (integer).

  Returns:
    The grade (A, B, C, D, or E).
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

# Get the student's score
score = int(input("Enter the student's score: "))

# Calculate and display the grade
grade = calculate_grade(score)
print(f"The grade is: {grade}")