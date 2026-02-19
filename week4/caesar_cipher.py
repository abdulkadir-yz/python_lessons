# In this example we gonna expalin ceasar algorithm in python. And understand how it works. With mahy examples and explain algorithm step by step.
# The Caesar Cipher is a simple encryption technique where each letter in the plaintext is shifted a certain
# number of places down the alphabet. For example, with a shift of 1, 'A' would be replaced by 'B', 'B' would become 'C', and so on.

def caesar_cipher(text, shift): #text is the our meesage or input message, shit is the number of positions we want to shift each letter in the text.
   
    result = "" # in first time we give the empty string to result variable

    for char in text: # in heree function check every charecter in text
        # Check if the character is a letter
        if char.isalpha(): # We dont want to all characters to be shifted, only letters. So we check if the character is a letter using the isalpha() method.
            # Determine if the letter is uppercase or lowercase to find its ASCII base
            # ASCII 'A' is 65, 'a' is 97
            ascii_base = ord('A') if char.isupper() else ord('a')
            
            # 1. Shift the character: (Current Position - Base + Shift)
            # 2. Use modulo 26 to wrap around (Z -> A)
            # 3. Add the base back to get the new ASCII value
            shifted_char = chr((ord(char) - ascii_base + shift) % 26 + ascii_base) # %26 because of alphabet has 26 letters
            result += shifted_char
        else:
            # If it's a space or punctuation, keep it as is
            result += char
            
    return result

# Test
unencripted_text = "Hello World"
shift_amount = 5
encrypted_text = caesar_cipher(unencripted_text, shift_amount)

print(f"Unencrypted Message: {unencripted_text}")
print(f"Encrypted Message: {encrypted_text}")