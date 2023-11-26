# BMI Calculator

Simple Python program to calculate Body Mass Index (BMI) for adults. The program asks the user for weight and height in either metric or imperial. The program was inspired by a health app on my iPhone thats linked to a smart scale that tracks changes in my weight.

The program contains helper functions that request the user for their height and weight that only takes in the float data type. Once the user has provided their weight and height, a function that calculates the BMI is called, this function uses the formula derived from the [CDC website](https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html)

Once the BMI has been calculated another function is called and the return value from the BMI calculation is checked against wight statuses provided by the CDC, if the user is at a healthy weight an emoji (smiling face with heart-eyes) is returned along with the rounded value of the users BMI.

# Usage

1. Run the python program by executing 'python bmi_calculator.py' in your terminal.
2. Enter your name when prompted.
3. Choose the system of units you would like to use (metric or imperial).
4. Enter your weight.
5. Enter your height.
6. The program will calculate your BMI and print your BMI and weight status.

# Functions

**system_of_units()**

This function prompts the user for either metric or imperial measurement system.

**get_height(system_units)**

The user is prompted for their height in meters / inches dependant on the selection made when the system_of_units() function was called.

**get_weight(system_units)**

The user is prompted for their weight in kg's / lbs dependant on the selection made when the system_of_units() function was called.

**calculate_bmi(system_units)**

The function calculates the BMI using the height and weight provided by the user in the get_height(system_units) and get_weight(system_units) helper functions. Below are the formulas dependant on the system of units selected at run time.

  **metric**

    bmi = weight / height ** 2

  **imperial**

    bmi = (weight / height ** 2) * 703

**weight_status(system_units)**

This function calculates the users weight status based on the BMI and returns one of the below status messages shown in the below table:



| BMI      | Status |
| ----------- | ----------- |
| Below 18.5       | Underweight        |
| 18.5 – 24.9    | Healthy Weight        |
| 25.0 – 29.9       | Overweight       |
| 30.0 and Above   | Obese       |