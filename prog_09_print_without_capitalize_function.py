# Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

# ask for user input
user_input = input("Enter a word: ")

if user_input: # check if its not empty
     first_char = user_input[0].upper() # convert first char into uppercase
     rest = user_input[1:].lower() # convert the rest to lowercase
     result = first_char + rest # combine
else: 
     result = ""

# display
print(result)