from utils.data_utils import calculate_bmi, validate_positive_number, validate_date, analyze_health
from utils.db_utils import create_table, insert_data

if __name__ == "__main__":
    create_table()

    # Collect user data
    name = input("Enter your name: ")
    age = validate_positive_number(input("Enter your age: "))
    gender = input("Enter your gender (Male/Female): ").strip().capitalize()
    weight = validate_positive_number(input("Enter your weight (in kg): "))
    height = validate_positive_number(input("Enter your height (in cm): "))
    date = validate_date(input("Enter the date (YYYY-MM-DD): "))

    if age and weight and height and date:
        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Collect additional health data
        steps_walked = validate_positive_number(input("Steps walked today: "))
        water_intake = validate_positive_number(input("Water intake (in liters): "))

        if steps_walked and water_intake:
            # Save data to the database
            insert_data(name, age, gender, weight, height, bmi, steps_walked, water_intake, date)

            # Analyze health
            health_status = analyze_health(bmi, steps_walked, water_intake, age, gender)

            # Display health analysis
            print("\nHealth Analysis Summary:")
            for status in health_status:
                print(f"- {status}")

            print("\nData saved successfully!")




