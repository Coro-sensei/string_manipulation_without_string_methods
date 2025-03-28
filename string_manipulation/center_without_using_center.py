# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

# Input character 
character = input("Enter your sentence: ")
width = 100

# Imitate center
center = width - len(character)
ljust = center // 2
rjust = center - ljust

centered_characters = "*" * ljust + character + "*" * rjust

# Print result
print(centered_characters)
