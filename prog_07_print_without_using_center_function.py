# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

# ask for user's input
user_input = input("Enter a word: ")

# ask for desired width
width = int(input("Enter the total width: "))

# calculate the space for centering 
if len(user_input) < width: 
    total_spaces = width - len(user_input)
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces
    user_input = " " * left_spaces + user_input + " " * right_spaces

# print display
print("Result:", user_input)