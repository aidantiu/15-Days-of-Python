# Write the code ↓ to prompt the user to enter a word.
# Be cautious when reading input of various data types.
print("CHECK VOWEL COUNTER FOR ALF\n")

words = input("Please, enter a word/s to check: ")

# Write the code ↓ to count the number of vowels in the entered word.
# Utilize string functions to iterate through the characters and identify vowels.
vowels = "aeiouAEIOU"
vowelCount = 0

for vowel in vowels:
    vowelCount += words.count(vowel)

# Write the code ↓ to display the count of vowels in the word.
# Select and employ a string concatenation method based on your personal preference and comfort level.
print(f"The number of vowels in '{words}' is: {vowelCount}")
