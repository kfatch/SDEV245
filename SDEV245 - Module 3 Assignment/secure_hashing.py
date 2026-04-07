#Kody Fatch
#SDEV245 Module 3 Assignment - Secure Hashing and Encryption
#This program will demonstrate the use of generating SHA-256 hashes for input strings.

import hashlib

def generate_hash(input):
    bytes = input.encode('utf-8')
    hash = hashlib.sha256(bytes)
    hashed_input = hash.hexdigest()
    return hashed_input

#-----------------Hashing Test-------------------------------------
user_input = input("Enter a string to hash:\n")
hashed_input = generate_hash(user_input)
print(f"SHA-256 hash of '{user_input}' is: {hashed_input}")