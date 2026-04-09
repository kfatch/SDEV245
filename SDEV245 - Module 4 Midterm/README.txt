Kody Fatch - SDEV245
README for Module 4 Midterm

-----------------Short Explanation of the principles of CIA used in this program-----------------
This program upholds the Confidentiality (C) and Integrity (I) of the CIA Triad in Cybersecurity. It does this by limiting the access of the program to only authorized users. It autenticates the user trying to login.
If the user's credientials match to one in the database, it next checks for authorization for access to the program. It authorization passes, then the user is granted access and is able to use the program.
This is the C of the CIA Triad in action. The other part of the Triad being used is the I. It checks the inital hash of the message trying to be sent using a generated Symmetric key against the decrypted hash
using the same key that was used to encrypt it. If the two hashes match, then the integrity of the message is upheld. If the hashes differ, then the integrity of the message has been compromised. 

-----------------------------Role of Entropy and Key Generation----------------------------------