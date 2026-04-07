Kody Fatch
SDEV245 - README file for Module 3 Code Assignment

I split the three deliverables for this assignment into individual python files. One that generates a SHA-256 hash for a user inputed string. The second that uses a substitution cipher to encrypt/decrypt 
an inputed text. And the final file simulates a digital signature (sign/verify). Below is the explanation and execution lines for each file. 

---------------------------securing_hashing-----------------------------------
This program takes a user input and uses the generate_hash() function and takes the input from the user as the parameter. The function converts the inputed string into bytes. It then uses the inported
hashlib to turn the bytes into a hash.

Terminal Output:
Enter a string to hash:
Hello There! General Kenobi.
SHA-256 hash of 'Hello There! General Kenobi.' is: 3964c99a25c1582eeb1ea8ed86e7289f01790e134f01e25e9c99e9d8b3383cb9
--------------------------substitution_cipher---------------------------------
This program uses two functions that encrypt and decrypt the user inputed message. The functions iterate through the strings inputed. It uses the ASCII, or the American Standard Code for
Information Interchange, and a single letter key that determines how the shift of each letter, character, or number changes. This program uses these results to change each letter, character and number of the string.

Terminal Output:
Enter text to encrypt:
Hello There! General Kenobi.
Original text: Hello There! General Kenobi.
Encrypted text: Lipps Xlivi! Kirivep Oirsfm.
Decrypted text: Hello There! General Kenobi.
---------------------------digital_signature----------------------------------
This program uses Asymmetric method of cryptography to create a public key and a private key to check if the integrity of the message inputed is intact. Two keys are generated and a message is inputed
by the user. The message is encrypted by the private key and the public key is used to verify the signature.

Terminal Output:
Enter the message to be signed:
Hello There! General Kenobi.
Message: Hello There! General Kenobi.
Signature: b'lc\xa3\xd2y\xa7\xf0\x99j\x87V\xa6\xe1,w5\x8fc\xff[\xc7\x98\xcf\xdf\xed\x84\xe0x\xab\xbc\xb5\x9f]y\xe8\x017\'l\xc0t\x91\x02\x98B\xecN|\r\x08\xd7\x84#\x87}s\xe7\xd3\x89\xabc\xda\x1f>\xf7
\x80\xa4#36\xf1\xb2G\xf4g\xe9\xe76Z<\xf6A&xA\xb9\x8e\xa7\x82\xc0\x9e\xd3\xc9\x02\x9c\xd5\xc2\'0"\xf1\xd7\xeaR}X\xc0\x12o\xaf\x04)\r\xfd\xd1\xf6\xde\'\xd7(l\x11\x13\x94e\x17\xa4\x90\xa2\xb2\xda\x89
\x8e\x12Un\xe4}h\xec@\x8b7\xf6dV\xc1\xb7\xe9K\x01\xb3\xf5\xa1~s6\x82d&2\xa9\x8b\xbc\xd1\xc5\xaat\xefT\xc7\xb1G\x0fgXqs\xac\xbd\x06!\x85a\xc1\xea\xd1\xcag\x97\xbb\x9d6w5\x01\xbd\xcc\xad\xf3Y\x85
\x88c~i\xb4\x89\x82.\'\x8d\xccs\xee\xc8\xd0\x89\x10f\x87:.\x8euX\xcf\xd4\xc2\\\xbbR\x9f\xe70\xa7}\x9aoG[\xdc\x858\x05\x91\xb6\xd3G\xfc]\xc0\xfcSh\xad'
Signature is valid.