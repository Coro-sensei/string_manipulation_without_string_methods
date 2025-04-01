# Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.

# Input character 
character = input("Enter your sentence: ")

# Imitate upper
pseudo_upper = ''.join(chr(ord(char) - 32) if 'A' <= char <= 'Z' else char for char in character)

# Print the result
print(pseudo_upper)
