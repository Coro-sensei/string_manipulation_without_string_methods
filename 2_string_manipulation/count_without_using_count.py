# Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

# Input character
sentence = input("Enter your sentence: ")
character_count = input("Enter what word to count : ")

# Imitate count
pseudo_counter = 0
for char in sentence:
    if char == character_count:
        pseudo_counter += 1
        
# Print result