 encryption = encryption + chr ((ord(letter) - 97 + ord(encKey[i % len(encKey)])-97 ) % 26 + 97) 
