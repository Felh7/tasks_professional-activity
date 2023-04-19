from hashlib import sha256
import rsa
(pubkey, privkey) = rsa.newkeys(1024)
hashed = sha256()
with open("key_s.pem", "wb") as file:
    file.write(pubkey.save_pkcs1())

with open ("практика 4_8 .txt", "rb") as f:
    cr = f.read()
    hashed.update(cr)
    message_hashed = hashed.digest()
    signed = rsa.sign(message_hashed, privkey, 'SHA-256')
with open ("gh.bin", "wb") as f:
    f.write(signed)
