# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

# ask for user's input
user_input = input("Enter a word: ")

# ask for the desired width
width = int(input("Enter the total width: "))

# add spaces at the end to match the given width
if len(user_input) < width: 
    user_input = user_input + " " * (width - len(user_input))

# print display
print("Result: ", user_input)
