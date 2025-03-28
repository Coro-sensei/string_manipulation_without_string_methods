# Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

# Input character
character = input("Enter your sentence: ")

# Imitate title
pseudo_title = " ".join(word[0].upper() + word[1: ].lower() if word else "" for word in character.split())

# Print result
print(pseudo_title)