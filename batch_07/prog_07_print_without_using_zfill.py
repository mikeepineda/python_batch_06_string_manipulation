# Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.

# ask for user's input
user_input = input("Enter a number or string: ")

# ask for desired width
width = int(input("Enter the total width: "))

def custom_zfill(string, width): # calculate how many zeros to add
    zeros_needed = width - len(string)  
    if zeros_needed > 0:
        return "0" * zeros_needed + string  
    return string

# print
print(f"'{custom_zfill(user_input, width)}'")