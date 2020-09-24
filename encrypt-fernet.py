#!/usr/bin/env python
import sys
import cryptography.fernet

key = cryptography.fernet.Fernet.generate_key()

print(f"key= {key}")
print(
    "Keep this some place safe! If you lose it you’ll no longer be able to decrypt messages; if anyone else gains access to it, they’ll be able to decrypt all of your messages, and they’ll also be able forge arbitrary messages that will be authenticated and decrypted."
)

crypt = cryptography.fernet.Fernet(key)

with open(sys.argv[1], 'rb') as fin:
    encoded = crypt.encrypt(fin.read())

with open(sys.argv[2], 'wb') as fout:
    fout.write(encoded)
