# Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

# Initiate the  lstrip
pseudo_lstrip = 0

# Input the characters 
character_input = input("Enter your sentence:")

# Imitate lstrip
while pseudo_lstrip < len(character_input) and character_input[pseudo_lstrip] == " ":
    pseudo_lstrip += 1
    
# Print the result
print(character_input[pseudo_lstrip: ])