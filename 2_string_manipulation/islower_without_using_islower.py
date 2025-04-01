# Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

# Input character
character = input("ENter your sentence: ")

# Imitate  islower
pseudo_islower = all('a' <= char <= 'z' for char in character if char.isalpha())

# Print result
