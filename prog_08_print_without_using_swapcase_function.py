# Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

# ask for user input
user_input = input("Enter a word: ")
result = ""

# loop every char
for char in user_input: 
# if char lowercase, subract 32 to become uppercase
# if char uppercase, add 32 to become lowercase
# if not letter, keep
# append to result
# print