#Kody Fatch
#SDEV245 - Module 4 Midterm - Secure Data Transmission App with Hashing and Encryption
#Section 2 of instructions are in the README file provided with this project. 
#-------------------Imports-----------------------
import hashlib
from cryptography.fernet import Fernet
#--------------------Functions--------------------
def hash_msg(msg):
    bytes = msg.encode('utf-8')
    hash = hashlib.sha256(bytes)
    hashed = hash.hexdigest()
    return hashed
def symmetric_key():
    key = Fernet.generate_key()
    crypto_key = Fernet(key)
    return key, crypto_key
def encrypt_msg(msg, key, crypto_key):
    encrypt_text = crypto_key.encrypt(msg.encode())
    return encrypt_text
def decrypt_msg(encrypted_msg, key, crypto_key):
    bytes = crypto_key.decrypt(encrypted_msg)
    decrypted_hash = bytes.decode('utf-8')
    return decrypted_hash
def verify_msg(hashed_msg, decrypted_hash):
    if hashed_msg == decrypted_hash:
        print("Message integrity verified: The original message has not been tampered with.")
    else:
        print("Message integrity verification failed: The original message may have been tampered with.")
#--------------------User_Database-----------------
user_list = {"user": {"password": "password123", "role": "user"}}
#--------------------Program-Code------------------
print("Welcome to the Secure Data Transmission App!")
print("This program will take a user message, hash it using SHA-256, encrypt the hash for secure transmission and finally decrypt and verify the message (hash comparison).")
user_msg = input("Please enter a message to transmit securely:\n")
hashed_msg = hash_msg(user_msg)                                  #Hashes the user message using SHA-256
key, crypto_key = symmetric_key()                                #Generates a symmetric key for encryption and decryption
encrypted_msg = encrypt_msg(hashed_msg, key, crypto_key)         #Encrypts the hashed message using the generated symmetric key
decrypted_hash = decrypt_msg(encrypted_msg, key, crypto_key)     #Decrypts the encrypted hash using the same symmetric key
verify_msg(hashed_msg, decrypted_hash)                           #Compares the original hash with the decrypted hash to verify message integrity
#-------------------Test-Output------------------------
print("--- Test Output ---")
print(f"Original Message: {user_msg}")
print(f"Hashed Message: {hashed_msg}")
print(f"Encrypted Hash: {encrypted_msg}")
print(f"Encryption Key: {key}")
print(f"Decrypted Hash Message: {decrypted_hash}")

#Login authentication of the user needed
#Final working neat version of the program deliverable
#Completion of the README file
#Video demonstration of the program working