# Program that opens a file and print its content.

# Read File
file = open("example.txt", "r")

# Print Content
content = file.read()
print(content)

# Close File
file.close()
