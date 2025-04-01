# Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.

# Input character
character = input("Enter your sentence: ")
suffix_cutter = input("Enter the prefix that you want to cut: ")

# Imitate removesuffix
if character.endswith(suffix_cutter):
    character = character.replace(suffix_cutter, "")

# Print result
print(character)
