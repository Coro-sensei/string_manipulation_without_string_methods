# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

# Input the character
character = input("Enter your sentence: ")
width = 100

# Imitate ljust
if len(character) < width:
    character += '*' * (width - len(character))

# Print result
print (f'{character}')