from hashlib import sha256 #hashlib
import rsa #rsa

(pubkey, privkey) = rsa.newkeys(1024) #создание ключей

hashed = sha256()

#запись открытого ключа в файл

with open("key_s.pem", "wb") as file:
    file.write(pubkey.save_pkcs1())

#хеширование исходных данных

with open ("практика 4_8 .txt", "rb") as f:
    cr = f.read()
    hashed.update(cr)
    message_hashed = hashed.digest()
    signed = rsa.sign(message_hashed, privkey, 'SHA-256')

#запись подписи в файл
with open ("gh.bin", "wb") as f:
    f.write(signed)
