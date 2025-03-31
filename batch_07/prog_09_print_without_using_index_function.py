# Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.

user_input = input("Enter a string: ")  # ask for user's input 
substring = input("Enter the substring to find: ")  # ask for substring

def custom_index(string, substring):    # def custom index
    for i in range(len(string) - len(substring) + 1):  # create loop
        if string[i:i + len(substring)] == substring:  # check for match
            return i  # return the first found index
    return -1 

# print