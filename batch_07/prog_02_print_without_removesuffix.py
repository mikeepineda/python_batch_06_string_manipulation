# Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.

string = input("Enter a string: ")
suffix = input("Enter the suffix to be removed: ")

if string.endswith(suffix): 
    string = string[:-len(suffix)]

print(f"'{string}'")