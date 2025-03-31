# Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.


# ask for user's input
user_input = input("Enter a word that ends with spaces: ")

# create loop
while user_input.endswith(" "):
    user_input = user_input[:-1]

# print 
print(f"'{user_input}'") 