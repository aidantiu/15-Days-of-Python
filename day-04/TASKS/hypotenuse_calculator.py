import math

# Write the code ↓ to read the lengths of the two shorter sides of a right-angled triangle from the user.
# Be cautious when reading input of various data types.
sideA = float(input("Please enter the length of side A: "))
sideB = float(input("Please enter the length of side A: "))

# Write the code ↓ to calculate the hypotenuse using the Pythagorean theorem.
# The Pythagorean theorem: c^2 = a^2 + b^2, where c is the hypotenuse.
hypotenuse = math.sqrt(sideA ** 2 + sideB ** 2)

# Write the code ↓ to display the calculated hypotenuse.
# Select and employ a string concatenation method based on your personal preference and comfort level.
print(f"The hypotenuse of the right-angled triangle is: {hypotenuse:.2f} ")
