# Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

# ask for user's input
user_input = input("Enter a word with leading spaces: ")

# find the first non-space character
index = 0
while index < len(user_input) and user_input[index] == ' ':
    index +=1

# slice the string from the first non-space character
# print