# Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

# Input character
character = input("Enter your sentence: ")
endswith = input("Enter the word that it should end with: ")

# Imitate endswith
result = False
if len(endswith) <= len(character): 
    if endswith == "":
        result = True
    else:
        result = character[-len(endswith): ] == endswith    
        

# Print result
print(result)
