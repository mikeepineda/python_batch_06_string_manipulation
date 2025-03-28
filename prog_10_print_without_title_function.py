# Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

# ask for user input
user_input = input("Enter a word: ")

# split input into words
words = user_input.split()
result = ""

for word in words: # loop each word
    first_char = word[0].upper() if word else ""    # capitalize first letter
    rest = word[1:].lower() if len(word) > 1 else "" # convert the rest to lowercase
    result += first_char + rest + " " # combine and add a space 

# print
print(result.strip())