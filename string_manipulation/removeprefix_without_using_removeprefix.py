# Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

# Input characters
character = input("Enter your word with a prefix: ")
prefix_cutter = input("Enter the prefix that you want to cut: ")

# Imitate removeprefix
if character.startswith(prefix_cutter):
    character = character.replace(prefix_cutter , "")

# Print result
print(character)