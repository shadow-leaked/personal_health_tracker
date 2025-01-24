from utils.data_utils import calculate_bmi, validate_positive_number, validate_date

# Test BMI Calculation
weight = 70  # in kg
height = 175  # in cm
bmi = calculate_bmi(weight, height)
print(f"BMI: {bmi}")

# Test Positive Number Validation
number = validate_positive_number(input("Enter a positive number: "))
if number:
    print(f"Valid number: {number}")

# Test Date Validation
date = validate_date(input("Enter a date (YYYY-MM-DD): "))
if date:
    print(f"Valid date: {date}")
