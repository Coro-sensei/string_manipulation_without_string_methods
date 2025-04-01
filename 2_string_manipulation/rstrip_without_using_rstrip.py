# Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

# Input characters
character_input = input("Enter your sentence: ")

# Imitate rstrip
pseudo_rstrip = len(character_input) - 1

while pseudo_rstrip >= 0 and character_input [pseudo_rstrip] == " ":
    pseudo_rstrip -= 1

# Print result
print(character_input[pseudo_rstrip: ])