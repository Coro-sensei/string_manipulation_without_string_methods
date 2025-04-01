# Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.

# Enter character
character = input("Enter your sentence: ")
pseudo_rindex = input("Enter what word to search: ")

# Imitate rindex
position = character.rfind(pseudo_rindex)

# Print result
if position != -1:
    print(f"This word '{pseudo_rindex}' is first found at {position}")
else:
    print(f"The word '{pseudo_rindex}' was not found")