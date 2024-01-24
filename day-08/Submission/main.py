# Program that reads csv and prints the values in the first column

import csv

# Open the file
with open("example1.csv", "r") as file:

    # Read the file
    csvReader = csv.reader(file)

    # Print the first column of the file
    for line in csvReader:
        print([line[0]])

# Program that reads json that prints its content 

import json

with open("example2.json", "r") as file:

    # Read the file
    jsonReader = json.load(file)

    # Store the content of file in data
    data =  json.dumps(jsonReader, indent=2)

    # Print the content of file
    print(data)




