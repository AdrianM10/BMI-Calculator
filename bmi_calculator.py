def main():
   name = input("What's your name? ")
   print(f"Hi {name} !", end="")
   system_units = system_of_units()

   bmi, status = weight_status(system_units)

   print(f"{name}, your BMI is {bmi}. You are currently {status}" )

def system_of_units():
    """Prompt user for Metric or Imperial System of measurement"""
    while True:
        response = input(" Will you be using 'Metric' or 'Imperial' units? ").lower()
        if response == 'metric':
            return response
        elif response == 'imperial':
            return response
        else:
            print("Invalid unit of measure provided")


def get_height(system_units):
    """Prompt user for height in meters (metric) or inches (imperial)"""
    if system_units == 'metric':
        try:
            height = float(input("Height in meters: "))
        except ValueError:
            print("Invalid input. Please enter a number")
        return height
    elif system_units == 'imperial':
        try:
            height = float(input("Height in inches: "))
        except ValueError:
            print("Invalid input. Please enter a number")
        return height


def get_weight(system_units):
    """Prompt user for weight in kg's (metric) or lbs (imperial)"""
    if system_units == 'metric':
        try:
            weight = float(input("Weight in kg's: "))
        except ValueError:
            print("Invalid input. Please enter a number")
    elif system_units == 'imperial':
        try:
            weight = float(input("Weight in lbs: "))
        except ValueError:
            print("Invalid input. Please enter a number")
    return weight

def calculate_bmi(system_units):
    """Calculate BMI using the formula"""
    weight = get_weight(system_units)
    height = get_height(system_units)
    # Metric
    if system_units == 'metric':
        bmi = weight / height ** 2
    # imperial
    elif system_units == 'imperial':
        bmi = (weight / height ** 2) * 703

    return bmi

def weight_status(system_units):
    """Get weight status from BMI"""
    bmi = calculate_bmi(system_units)

    if bmi < 18.5:
        return round(bmi, 2), "underweight 😭 "
    elif bmi >= 18.5 and bmi <= 24.9:
        return round(bmi, 2), "healthy 😍"
    elif bmi >= 25.0 and bmi <= 29.9:
        return round(bmi, 2), "overweight 😭"
    else:
        return round(bmi, 2), "obese 😭"


if __name__ == "__main__":
    main()