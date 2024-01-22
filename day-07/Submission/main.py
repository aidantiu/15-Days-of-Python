# Program that writes on a file and print if its done.

# Write File
file = open("user_info.txt", "w")

# Print Content
content = file.write(input("Please input your name: "))
print("Done!")

# Close File
file.close()

