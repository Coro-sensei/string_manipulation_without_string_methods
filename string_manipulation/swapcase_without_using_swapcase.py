# Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

# Input character
character = input("Enter your sentence: ")

# Imitate swapcase
pseudo_swapcase = "".join(char.lower() if char.isupper() else char.upper() for char in character)

# Print result
print(pseudo_swapcase)