# BMI - NUTRITIONAL STATUS GUIDE
"""
    BMI         NUTRITIONAL STATUS

BELOW 18.5         UNDERWEIGHT
18.5 - 24.9       NORMAL WEIGHT
25.0 - 29.9        OVERWEIGHT
ABOVE 30.0          OBESITY
"""

# Write the code ↓ to read user's height and weight.
# Be cautious when reading input of various data types.
print("BMI CALCULATOR FOR ALF\n")
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Write the code ↓ to perform the calculations of user's BMI and categorize its status.
bmi = weight / height ** 2

# Write the code ↓ to display the user's BMI and its classification.
# Select and employ a string concatenation method based on your personal preference and comfort level.
# Use :.2f format specifier when printing the BMI value to display the BMI with only two decimal places.
print(f"HEIGHT: {height} - WEIGHT: {weight}")
print(f"BMI: {bmi:.2f} - WEIGHT: {weight} - ", end="")

if bmi < 18.5:
    print("NUTRITIONAL STATUS: Underweight")
elif 18.5 < bmi < 24.9:
    print("NUTRITIONAL STATUS: Normal Weight")
elif 25.0 < bmi < 29.9:
    print("NUTRITIONAL STATUS: Overweight")
elif bmi > 30.0:
    print("NUTRITIONAL STATUS: Obesity")

