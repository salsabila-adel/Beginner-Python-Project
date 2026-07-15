# Encrypt your Word


import random
import string

chars=string.punctuation+string.digits+string.ascii_letters+" "

chars=list(chars)
key=chars.copy()
random.shuffle(key)


# Encrypt
plain_text=input("Enter your Message to encrypt: ")
cipher_text=""

for letter in plain_text:
    ind=chars.index(letter)
    cipher_text+=key[ind]
print(cipher_text)

# Decrypt
cipher_text=input("Enter your Message to decrypt: ")
plain_text=""

for letter in cipher_text:
    ind=key.index(letter)
    plain_text+=chars[ind]
print(plain_text)

