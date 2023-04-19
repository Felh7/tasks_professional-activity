import rsa
from hashlib import sha256
hashed = sha256()

with open("key_s.pem", "rb") as file:
    keydata = file.read()
pubkey = rsa.PublicKey.load_pkcs1(keydata)

with open("gh.bin", "rb") as file:
    signed = file.read()
with open("практика 4_8 .txt", "rb") as file:
    buf = file.read()
    hashed.update(buf)
    hashed_message= hashed.digest()
try:
    if rsa.verify(hashed_message, signed, pubkey):
        print("успешно")
except rsa.VerificationError:
    print("неуспешно")
