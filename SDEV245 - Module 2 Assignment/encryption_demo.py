#Kody Fatch
#This program demonstrates the encryption and decryption of a given message using symmetric key encryption (AES) and asymmetric key encryption (RSA).
# It allows the user to enter a message, encrypt it, and then decrypt it using both methods.

#Imports
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
#Functions
def start():
    print("This program demonstrates symmetric and asymmetric encryption methods.")
    msg = input("You can enter a message, and it will be encrypted and decrypted using both methods.\n")
    return msg
def message():
    print("Entering a new phrase will replace the previous one.")
    msg = input("Enter the message you want to use for cryptography:\n")
    return msg
def symmetric_key():
    key = Fernet.generate_key()
    crypto_key = Fernet(key)
    return key, crypto_key
def symmetric_method(msg, crypto_key, key):
    print(f"Original message: {msg}")
    print(f"Encryption key: {key.decode()}")
    #Encrypting the message
    msg_bytes = msg.encode()
    encrypted_msg = crypto_key.encrypt(msg_bytes)
    print(f"Encrypted message: {encrypted_msg.decode()}")
    #Decrypting the message
    decrypted_msg_bytes = crypto_key.decrypt(encrypted_msg)
    decrypted_msg = decrypted_msg_bytes.decode()
    print(f"Decrypted message: {decrypted_msg}")
def asymmetric_key():
    private_key = rsa.generate_private_key(public_exponent=65537,key_size=1024)
    public_key = private_key.public_key()
    return public_key, private_key
def asymmetric_method(msg):
    print(f"Original message: {msg}")
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")
    #Encryption
    msg_bytes = msg.encode('utf-8')
    encrypted_msg = public_key.encrypt(msg_bytes, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    print(f"Encrypted message: {encrypted_msg}")
    #Decryption
    decrypted_msg_bytes = private_key.decrypt(encrypted_msg, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    decrypted_msg = decrypted_msg_bytes.decode('utf-8')
    print(f"Decrypted message: {decrypted_msg}")

#Main
msg = start()
key, crypto_key = symmetric_key()
symmetric_method(msg, crypto_key, key)
public_key, private_key = asymmetric_key()
asymmetric_method(msg)