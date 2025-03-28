# Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

# ask for user's input
# ask the user what prefix to removed
user_input = input("Enter your word: ")
prefix = input("Enter a prefix to be removed: ")

# check if the user's input starts with a prefix
if user_input.startswith(prefix):
    user_input = user_input[len(prefix):] # remove the prefix by slicing

# print
print(user_input)
