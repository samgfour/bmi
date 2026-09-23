# BMI Calculator with unit conversion

def calculate_bmi(weight, height, unit_type="metric"):
    if weight is None or height is None:
        raise ValueError("Weight and height are required.")
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be greater than zero.")

    if unit_type == "imperial":
        # Convert pounds to kilograms and inches to meters
        weight = weight * 0.453592  # pounds to kg
        height = height * 0.0254    # inches to meters
    elif unit_type != "metric":
        raise ValueError("unit_type must be 'metric' or 'imperial'.")

    # BMI formula: weight (kg) / (height (m))^2
    return weight / (height ** 2)


def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"


def _prompt_for_float(prompt_text):
    while True:
        try:
            value = float(input(prompt_text))
            if value <= 0:
                print("Please enter a value greater than zero.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("Welcome to the BMI Calculator!")

    while True:
        unit_type = input("Choose unit system (metric/imperial): ").strip().lower()
        if unit_type in ["metric", "imperial"]:
            break
        print("Invalid input. Please choose either 'metric' or 'imperial'.")

    if unit_type == "metric":
        weight = _prompt_for_float("Enter your weight in kilograms: ")
        height = _prompt_for_float("Enter your height in meters: ")
    else:  # imperial
        weight = _prompt_for_float("Enter your weight in pounds: ")
        height = _prompt_for_float("Enter your height in inches: ")

    try:
        bmi = calculate_bmi(weight, height, unit_type)
        category = interpret_bmi(bmi)
    except ValueError as exc:
        print(f"Error: {exc}")
        return

    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")


if __name__ == "__main__":
    main()
