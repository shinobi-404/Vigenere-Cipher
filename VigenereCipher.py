# /*=============================================================================
# | Encrypting a plaintext file using the Vigenere cipher
# | or python -> python pa01.py kX.txt pX.txt
# | where kX.txt is the keytext file
# | and pX.txt is plaintext file
# |
# | Note: All input files are simple 8 bit ASCII input
# |
# +=============================================================================*/


import sys
import re


# takes the plain text and the encription key to create an encryption using the viegenre cipher
def encrypt(plaintxt, encKey):
    encryption = ""
    # runs trough each character and encrpyts it accoding to the formula 
    for i in range(len(plaintxt)):
        letter = plaintxt[i] 
        # C = E (K, P) = (Pi + Ki) mod 26 for Vigener cipher
        encryption = encryption + chr ((ord(letter) - 97 + ord(encKey[i % len(encKey)])-97 ) % 26 + 97) 

    return encryption


# organizes 80 characters per line 
def printStatement(plaintxt):
    for i in range(len(plaintxt)):
        if i % 80 == 0: # shows lines that work with 80 characters per line
            print("")
        print(plaintxt[i],end= "")


def main():

    if len(sys.argv) < 3:
        return 
    # take the file containing the key and plaintext 
    inputfile = sys.argv[1]
    outputfile = sys.argv[2]

    # reads key file and removes non-alphabetic characters and converts them to lowercase 
    encKey_file = open(inputfile,'r') #opens file
    encKey = encKey_file.read() # reads file
    encKey = re.sub(r'[^a-zA-Z]','',encKey).lower()

    # reads plain text file and removes non-alphabetic characters and converts them to lowercase 
    plaintxt_file = open(outputfile,'r', encoding="utf8") # opens file 
    plaintxt = plaintxt_file.read() # reads file
    plaintxt = re.sub(r'[^a-zA-Z]','',plaintxt).lower() # gets rid of non-alphabetic characters

    # prints the Vigenere key
    print("\n\nVigenere Key:")
    printStatement(encKey) # displays the key
    print("")
    
    # keeps text at 512 characters 
    while len(plaintxt) < 512:
        plaintxt += "x" # added x as padding 

    # limits characters to 512 in text 
    if len(plaintxt) > 512:
        plaintxt = plaintxt[:512]
    
    # displays plain text
    print("\n\nPlaintext:")
    printStatement(plaintxt) #displays the plain text 

    # displays encrypted msg
    encryptedMsg = encrypt(plaintxt,encKey) # functions takes in plain text and the key to create a cipher, returns encrypted message 
    print("\n\n\nCiphertext:")
    printStatement(encryptedMsg) # displays the encrypted message 
    print("")

    
if __name__ == "__main__":
    main() # calls main function 


import sys
# import numpy as np
# import pandas as pd
# from sklearn import ...

for line in sys.stdin:
    print(line, end="")