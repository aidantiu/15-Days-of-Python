# Write the code ↓ to read the user's input for a non-negative integer.
# Be cautious when reading input of various data types.
print("FACTORIAL CALCULATOR FOR ALF \n")

# Write the code ↓ to calculate the factorial of the user-defined integer using a loop.
userInp = int(input("Please, enter a non-negative integer: "))

if userInp < 0:
    print("Enter a non-negative integer.")

factorial = 1
for factor in range(1, userInp + 1):
    factorial *= factor

# Write the code ↓ to display the factorial result.
print(f"The factorial of {userInp} is: {factorial}")
# Select and employ a string concatenation method based on your personal preference and comfort level.

