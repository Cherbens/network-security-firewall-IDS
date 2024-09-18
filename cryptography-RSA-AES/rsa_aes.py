# RSA and AES encryption example in Python

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# RSA key generation
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# AES encryption
key_aes = get_random_bytes(16)
aes_cipher = AES.new(key_aes, AES.MODE_EAX)
ciphertext, tag = aes_cipher.encrypt_and_digest(b'Secret Message')