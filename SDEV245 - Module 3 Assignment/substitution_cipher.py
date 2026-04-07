#Kody Fatch
#SDEV245 Module 3 Assignment - Secure Hashing and Encryption
#This program will demonstrate using substitution cipher to encrypt/decrypt input.

def encrypt(text, key):
    message = ""
    for char in text:
        if char.isalpha():
            shift = ord(key) - ord('a')
            if char.islower():
                message += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                message += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            message += char
    return message

def decrypt(text, key):
    message = ""
    for char in text:
        if char.isalpha():
            shift = ord(key) - ord('a')
            if char.islower():
                message += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                message += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            message += char
    return message

# Example usage
key = "K"
plaintext = input("Enter text to encrypt:\n")
encrypted_text = encrypt(plaintext, key)
decrypted_text = decrypt(encrypted_text, key)

print(f"Original text: {plaintext}")
print(f"Encrypted text: {encrypted_text}")
print(f"Decrypted text: {decrypted_text}")