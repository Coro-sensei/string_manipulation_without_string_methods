# Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.

# Input character
character = int(input("Enter your number: "))
width_of_zero = int(input("Enter your desired amount of zero to fill: "))

# Imitate zfill
pseudo_zfill = "0" * (width_of_zero - len(character)) + character if len(character) < width_of_zero else character

# Print result
print(pseudo_zfill)