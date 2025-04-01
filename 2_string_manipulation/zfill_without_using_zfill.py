# Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.

# Input character
character = input("Enter your characters: ")
width_of_zero = int(input("Enter your desired amount of total zero to fill: "))

# Imitate zfill
pseudo_zfill = "0" * (width_of_zero - len(character)) + character if len(character) < width_of_zero else character

# Print result
print(pseudo_zfill)