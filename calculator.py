# BMI Calculator with unit conversion
def calculate_bmi(weight, height, unit_type="metric"):
    if unit_type == "imperial":
        # Convert pounds to kilograms and inches to meters
        weight = weight * 0.453592  # pounds to kg
        height = height * 0.0254    # inches to meters
    
    # BMI formula: weight (kg) / (height (m))^2
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator!")
    
    # Select unit system
    unit_type = input("Choose unit system (metric/imperial): ").strip().lower()
    while unit_type not in ["metric", "imperial"]:
        print("Invalid input. Please choose either 'metric' or 'imperial'.")
        unit_type = input("Choose unit system (metric/imperial): ").strip().lower()
    
    # Get user input
    if unit_type == "metric":
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
    else:  # imperial
        weight = float(input("Enter your weight in pounds: "))
        height = float(input("Enter your height in inches: "))
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height, unit_type)
    
    # Interpret the result
    category = interpret_bmi(bmi)
    
    # Output the result
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()
    
