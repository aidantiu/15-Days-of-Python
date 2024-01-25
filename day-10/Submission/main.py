import csv
import json

# Prompt user for name, age, and favorite food
name = input("Enter your name: ")
age = input("Enter your age: ")
Favoritefood = input("Enter your favorite food: ")

# Create a dict in json
user_data = {
    "name": name,
    "age": age,
    "favorite_food": Favoritefood
}

# Store content
jsonContent = json.dumps(user_data, indent=4)

# Display Content
print(jsonContent)

# Write to file
with open("output.json", "w") as json_file:
    json_file.write(jsonContent)
   


