# Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.

# Input character
character = str(input("Enter your sentence: "))
width = 100

# Imitate rjust
if len(character) < width:
    character = '*' * (width - len(character)) + character

# Print result
print(f'{character}')