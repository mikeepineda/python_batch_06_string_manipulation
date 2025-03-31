# Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

# ask for user input
user_input = input("Enter a string: ")
# ask for substring
substring = input("Enter the substring to count: ")

# def custom count
def custom_count(string, substring):
    count = 0
    index = 0

# create loop
    while index <= len(string) - len(substring):  # Loop through string
        if string[index:index + len(substring)] == substring:  # Match found
            count += 1
        index += 1  # Move to the next character

    return count

# print
print(f"'{substring}' appears {custom_count(user_input, substring)} times in '{user_input}'.")
