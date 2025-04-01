# Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.

# Input character
character = input("Enter your sentence: ")
startswith = input("Enter what your sentence should start with: ")

# Imitate startswith
result = False
if len(startswith) <= len(character): 
    if startswith == "":
        result = True
    else:
        result = character[:len(startswith)] == startswith    

# Print result 
print(result)