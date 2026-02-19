# In this example we gonna expalin ceasar algorithm in python.
# The Caesar Cipher is a simple encryption technique where each letter in the plaintext is shifted a certain
# number of places down the alphabet. For example, with a shift of 1, 
# 'A' would be replaced by 'B', 'B' would become 'C', and so on.

def caesar_cipher(text, shift):#text is the our meesage or input message, shit is the number of positions we want to shift each letter in the text.

    result = ""  # in first time we give the empty string to result variable

    # Loop through every character in the text
    for char in text: #We check every letter one by one

        # First, check if it is a letter
        if char.isalpha(): # Here we check is this letetr. ".isalpha" check this., 

            # Check if the letter is uppercase
            if char.isupper(): #
                alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ"
                alphabet = alphabet_upper
            else:
                alphabet_lower = "abcdefghijklmnopqrstuvwxyzäöüß"
                alphabet = alphabet_lower

            # Find the position of the letter in the alphabet
            index = alphabet.find(char) # for example if char = B, Position =2

            # Move the letter forward by 'shift'
            new_index = index + shift # if shift = 5, B(1) becomes G(6)

            # If the new index is bigger than alphabet length, wrap around
            while new_index >= 26:  # if we pass the Z ,we go back A
                new_index = new_index - 26

            # Get the new letter from alphabet
            new_char = alphabet[new_index]

            # Add the new letter to result
            result = result + new_char

        else:
            # If it is not a letter (space, punctuation), keep it same
            result = result + char

    return result

message = "Hello World , My name is Kadir."
shift_value = 5

encrypted = caesar_cipher(message, shift_value)

print("Unencrypted:", message)
print("Encrypted:", encrypted)