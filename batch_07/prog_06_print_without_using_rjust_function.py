# Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.

# ask for user's input
string = input("Input string: ")

# ask for the desired width
width = int(input("Enter the total width: "))

# add spaces at the start to match the given width
if len(string) < width:
    string = " " * (width - len(string)) + string

# print display
print(f"Result: '{string}'")
