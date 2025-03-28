# Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

# Input characters
character = input("Enter your sentence: ")

# Imitate isupper
pseudo_isupper = all('A' <= char <= 'Z' for char in character if char.isalpha())

# Print result
