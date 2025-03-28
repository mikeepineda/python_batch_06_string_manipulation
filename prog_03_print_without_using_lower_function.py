# Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

# ask for user's input
user_input = input("Input a word: ")

def to_lowercase(user_input):
    result = ""
    for char in user_input:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": # check if the character is uppercase
            result += chr(ord(char) + 32) # convert to lowercase using ORD
        else: 
            result += char # don't change the non-uppercase
    return result

# print result
print(to_lowercase(user_input))