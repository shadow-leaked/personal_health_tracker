from datetime import datetime

# 1. Calculate BMI
def calculate_bmi(weight, height):
    """
    Calculate BMI using the formula: weight (kg) / height (m)^2
    """
    try:
        height_m = height / 100  # Convert height from cm to meters
        bmi = weight / (height_m ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        print("Height cannot be zero.")
        return None

# 2. Validate Positive Numbers
def validate_positive_number(value):
    """
    Ensure the input is a positive number (int or float).
    Raises ValueError if invalid.
    """
    try:
        number = float(value)
        if number <= 0:
            raise ValueError("Value must be greater than 0.")
        return number
    except ValueError:
        print(f"Invalid input: {value}. Please enter a positive number.")
        return None

# 3. Validate Date
def validate_date(date_str):
    """
    Validate if the input string is in the format YYYY-MM-DD.
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return None

# 4. Transform Data for Visualization (Optional)
def transform_data_for_visualization(data):
    """
    Convert raw database records into a format suitable for visualization.
    Example: Transform a list of tuples into dictionaries with named fields.
    """
    transformed_data = []
    for record in data:
        transformed_data.append({
            "date": record[0],
            "steps_walked": record[1],
            "water_intake": record[2],
            "bmi": record[3],
        })
    return transformed_data


def analyze_health(bmi, steps_walked, water_intake, age, gender):
    """
    Analyze the user's health based on BMI, steps walked, and water intake.
    Returns a summary of health status.
    """
    health_status = []

    # 1. Analyze BMI
    if bmi < 18.5:
        health_status.append("Underweight")
    elif 18.5 <= bmi <= 24.9:
        health_status.append("Normal weight")
    elif 25 <= bmi <= 29.9:
        health_status.append("Overweight")
    else:
        health_status.append("Obese")

    # 2. Analyze Steps Walked
    recommended_steps = 10000
    if steps_walked < recommended_steps:
        health_status.append(f"Low activity (walked {steps_walked} steps, less than {recommended_steps})")
    else:
        health_status.append(f"Active (walked {steps_walked} steps, met the daily goal)")

    # 3. Analyze Water Intake
    if gender.lower() == "male":
        recommended_water = 3  # in liters
    else:
        recommended_water = 2.2  # in liters

    if water_intake < recommended_water:
        health_status.append(f"Dehydrated (drank {water_intake}L, less than {recommended_water}L recommended)")
    else:
        health_status.append(f"Well hydrated (drank {water_intake}L, met the daily goal)")

    # 4. Provide Overall Summary
    if "Underweight" in health_status or "Obese" in health_status:
        health_status.append("Overall health: Needs improvement")
    elif "Low activity" in health_status or "Dehydrated" in health_status:
        health_status.append("Overall health: Moderate, try to improve daily goals")
    else:
        health_status.append("Overall health: Good, keep it up!")

    return health_status
