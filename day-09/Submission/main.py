# Program that opens a file and counts and print the no. of lines in it

# Open the file
file = open("story.txt", "r")

# Read the no. of lines in the file
numLines = file.readlines()

# Print the no. of lines in the file
print(len(numLines))

# Close the file
file.close()
