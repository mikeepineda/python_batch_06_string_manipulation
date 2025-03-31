# Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.

# ask for user's input
user_input = input("Enter a word: ")

# ask for the prefix
prefix = input("Enter your prefix: ")

# extract the first part of the input using slicing
# compare with prefix
if user_input[:len(prefix)] == prefix:
    print("The string starts with the given prefix.")   # print display
else:
    print("The string does NOT start with the given prefix.")