# Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

# Input character
character = str(input("Enter your sentence: "))

# Imitate capitalize
if character: 
    pseudo_capitalize = character[0].upper() + character[1:].lower()
else:
    pseudo_capitalize = ""

# Print result 
print(pseudo_capitalize)