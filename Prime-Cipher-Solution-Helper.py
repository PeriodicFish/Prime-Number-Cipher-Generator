def subtract_from_letter(letter, number):
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    if letter in lowercase:
        index = lowercase.index(letter)
        new_index = (index - number) % 26
        return lowercase[new_index]
    elif letter in uppercase:
        index = uppercase.index(letter)
        new_index = (index - number) % 26
        return uppercase[new_index]
    else:
        return letter  # Return the character as is if it's not a letter

# Get user input
letter = input("Enter a letter: ")
number = int(input("Enter a number to subtract: "))

# Perform the subtraction
result = subtract_from_letter(letter, number)

# Display the result
print(f"{letter} - {number} = {result}")
