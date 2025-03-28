# Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

# Input characters
character = input("Enter your sentence to be uncapitalized: ")

# Imitate lower
pseudo_lower = [chr(ord(char) + 32) if 'A' <= char <= 'Z' else char for char in character]

# Print result