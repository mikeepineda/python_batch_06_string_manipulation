# Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

# ask for user's input
user_input = input("Enter a word: ")

# check if the input is in lowercase, return false
def custom_isupper(user_input):
    for char in user_input:
        if char in "abcdefghijklmnopqrstuvwxyz":
            return False
# else return true
    return True

# check if the input is uppercase
if custom_isupper(user_input):
    print("All characters are uppercase.") # display result
else: 
    print("Not all characters are uppercase.")  