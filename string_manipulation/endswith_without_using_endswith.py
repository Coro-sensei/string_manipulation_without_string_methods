# Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

# Input character
character = input("Enter your sentence: ")
endingwith = input("Enter the character the sentence should end with: ")

# Imitate endswith
pseudo_endswith = character[-len(endingwith)] == endingwith

# Print result