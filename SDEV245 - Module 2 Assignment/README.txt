Kody Fatch - SDEV245 SPRING 2nd 8-WEEKS
Module 2 Assignment - Encrypt/Decrypt Demo README

The funcitonality of my coded in this assignment is to learn and practice encryption and decryption of a user-inputed message using both Symmetric and Asymmetric methods.
The Symmetric method involves generating a key that is used to both encrypt and decrypt a given string. In my program, I used a function to generate a key and then a separate function to encrypt and decrypt
a message. The string entered by the user was "Hello There!" and it had to be encoded into bytes before encryption. And after the encryption it had to be decoded back into a string so that it can be decrypted. 
The process is similar to Asymmetric with the difference being that two different keys are used with encryption and decryption. Below are the input, output, and keys associated with my test run of the program. 

--------------Symmetric---------------------
Original message: Hello There!
Encryption key: wotpS8Y5PKtdxs6S2_Balt0sJM8uA3pfei6f3Y3hpt4=
Encrypted message: gAAAAABpywlKZVvg6tmJqp4-GNzGTxfr8UmPmtMrd37toE3WKKZtSo0b5EvrqdtSyAW7ERH0SA1abiMFdHpBiTmi4nc49_WRKA==
Decrypted message: Hello There!

----------------Asymmetric------------------
Original message: Hello There!
Public Key: <cryptography.hazmat.bindings._rust.openssl.rsa.RSAPublicKey object at 0x0000020CC23A64B0>
Private Key: <cryptography.hazmat.bindings._rust.openssl.rsa.RSAPrivateKey object at 0x0000020CC23A5E30>
Encrypted message: b'\xaaH\x83Y\xf6\x80\xed\xc8\xde\xc3F\xc918\xcc^\x03j2\x8eMZ\xdeN\xd9\x13\x08{\x18\x86\xd4+K\xb8\xcd^\x88O\x88\x84\xe2L\xbcp\x1e\xaf(>\xd2_\x17O\x9e\xd0\xc6:\xe8 V\x02C\xf5\x10\x95\x95\x93c\xe1\xeb\x019\xbf\xb3H\x8b5V\xef\x06j\x00\xceN\xb7\x92\xce\x82\xfa\xa2\xeb\xff\xec\x94Z\xc9^\xc4\xd2\xb9\x13\\\xb4sc|\xe1;X\x01\xbe\xfc$\x135W\xbb\xbe\xca4\x92aw\x1d\xd0\xe2tm\x88'
Decrypted message: Hello There!