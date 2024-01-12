# Write the code ↓ to read user's input for two operands and selected operation.
# NOTE: The two operands must be read as floats.
print("SIMPLE CALCULATOR FOR ALF\n")
firstNum = float(input("Enter the first number: "))
secondNum = float(input("Enter the second number: "))
operator = str(input("Enter the operator (+, -, x, /): "))

# Write the code ↓ to perform the calculations based on the selected operation.
if operator == "+":
    result = firstNum + secondNum
elif operator == "-":
    result = firstNum - secondNum
elif operator == "x":
    result = firstNum * secondNum
elif operator == "/":
    result = firstNum / secondNum
    # Check if denominator is 0
    if secondNum == 0:
        print("Cannot divide by 0.")
else:
    print("Enter a valid operator.")

# Write the code ↓ to display the result.
print(f"\nThe result of {firstNum} {operator} {secondNum} is {result}")

# Select and employ a string concatenation method based on your personal preference and comfort level.
