import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"chars   : {chars}")
print(f"key     : {key}")

# encryption
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index] # get the corresponding letter from the key

print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")

# decryption
chipper_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in chipper_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted message: {chipper_text}")
print(f"decrypted message: {plain_text}")