# Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.

# ask for user's input
user_input = input("Input a word: ")

def to_uppercase(user_input):
    result = ""
    for char in user_input:
        if char in "abcdefghijklmnopqrstuvwxyz": # check if the character is lowercase
            result += chr(ord(char) - 32) # convert to uppercase using ORD
        else: 
            result += char # don't change the non-lowercase
    return result

# print result
print(f"'{to_uppercase(user_input)}'")