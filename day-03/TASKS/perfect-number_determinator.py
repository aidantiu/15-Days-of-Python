# Write the code ↓ to read the user's input for a positive integer.
# Be cautious when reading input of various data types.
print("PERFECT NUMBER DETERMINATOR FOR ALF\n")

userInp = int(input("Please enter a positive integer: "))

if userInp < 0:
    print("Enter a positive integer.")

# Write the code ↓ to check if the entered integer is a Perfect Number using a loop.
perfectNumber = 0
for num in range(1, userInp):
    if userInp % num == 0:
        perfectNumber += num

# Write the code ↓ to display the Perfect Number check result.
# NOTE : You can use if-else statement or ternary operator to display the result.

if perfectNumber == userInp:
    print(f"{userInp} is a perfect number")
else:
    print(f"{userInp} is not a perfect number")





