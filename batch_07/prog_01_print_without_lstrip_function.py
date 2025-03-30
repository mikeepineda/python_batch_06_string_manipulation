# Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

# ask for user's input
text = input("Enter a word: ")

# initialize i to zero
# create loop

def remove_leading_spaces(s): 
    i = 0
    while i < len(s) and s[i] == ' ':
        i += 1
    return s[i:]

result = remove_leading_spaces(text)

# print result
print(result)