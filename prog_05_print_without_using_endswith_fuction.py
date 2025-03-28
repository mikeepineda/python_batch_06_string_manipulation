# Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

# ask for user's input
user_input = input("Enter a word: ")

# ask for the suffix 
suffix = input("Enter your suffix: ")

# check if the end of text matches the suffix
# extract the last part of the input using slicing
# compare with suffix
# store the result
result = text[-len(suffix):] == suffix

# print display
print("Ends with suffix", result)