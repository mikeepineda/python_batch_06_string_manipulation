# Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

# ask for user's input
user_input = input("Enter a word: ")

# check if the input is in uppercase, return false
def custom_islower(user_input):
    for char in user_input:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return False
# else return true
    return True

# check if the input is uppercase
# display result
