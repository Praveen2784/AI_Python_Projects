def can_administer_medicine(age, weight=None):

  if age >= 18:
    return "Medicine can be administered (adult)."
  elif age >= 15 and weight is not None and weight >= 55:
    return "Medicine can be administered (age and weight criteria met)."
  else:
    return "Medicine cannot be administered based on the given criteria."

# Get patient's age
age = int(input("Enter the patient's age: "))

# If age is 15-17, ask for weight
if 15 <= age < 18:
  weight = int(input("Enter the patient's weight in kilograms: "))
  result = can_administer_medicine(age, weight)
else:
  result = can_administer_medicine(age)

print(result)