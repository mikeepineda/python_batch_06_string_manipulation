# Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

# ask for user's input
user_input = input("Enter a word: ")

# ask for the suffix 
suffix = input("Enter your suffix: ")

# check if the end of text matches the suffix
# extract the last part of the input using slicing
# compare with suffix
# print display
if user_input[-len(suffix):] == suffix:
    print("The string ends with the given suffix.")
else:
    print("The string does NOT end with the given suffix.")