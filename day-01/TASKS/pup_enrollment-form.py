# Write the code ↓ to read user's input.
# Be cautious when reading input of various data types.
print("PUP Enrollment Form\n")
fullName = str(input("Enter your full name: "))
age = int(input("Enter your age: "))
gwa = float(input("Enter your previous general weighted average: "))
isMember = bool(input("Are you a member of AWS Cloud Club? (yes/no): ").lower() == "yes")

# Write the code ↓ to display the user's personal information.
print("\nYour Enrollment Form:")

# Select and employ a string concatenation method based on your personal preference and comfort level.
print(f"Name: {fullName}")
print(f"Age: {age}")
print(f"GWA: {gwa}")
print(f"Awstraunot: {isMember}")




