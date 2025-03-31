# Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.

user_input = input("Enter a string: ")  # ask for user's input 
substring = input("Enter the substring to find: ")  # ask for substring

def custom_rindex(string, substring):
    for i in range(len(string) - len(substring), -1, -1):  #loop backward
        if string[i:i + len(substring)] == substring: 
            return i  # return the last found index
    return -1  # return -1 if not found

index = custom_rindex(user_input, substring)

# print
if index != -1:
    print(f"'{substring}' last found at index {index} in '{user_input}'.")
else:
    print(f"'{substring}' not found in '{user_input}'.")