# Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.

# Input character
character = input("Enter your sentence: ")
pseudo_index = input("Enter what word to search: ")

# Imitate index
position = character.find(pseudo_index)

#  Print result 
if position != -1:
    print(f"This word '{pseudo_index}' is first found at {position}")
else:
    print(f"The word '{pseudo_index}' was not found")
