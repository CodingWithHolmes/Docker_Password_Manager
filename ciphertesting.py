from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import sys


def encrypt():
    data = 'secret data to transmit'.encode()
    print(data)

    aes_key = get_random_bytes(16)
    print(aes_key)

    cipher = AES.new(aes_key, AES.MODE_OCB)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    assert len(cipher.nonce) == 15

    print(ciphertext)

    with open("encrypted.bin", "wb") as f:
        f.write(tag)
        f.write(cipher.nonce)
        f.write(ciphertext)

    return aes_key

    # Share securely aes_key and hmac_key with the receiver
    # encrypted.bin can be sent over an unsecure channel


def decrypt(aes_key):
    # Somehow, the receiver securely get aes_key and hmac_key
    # encrypted.bin can be sent over an unsecure channel

    with open("encrypted.bin", "rb") as f:
        tag = f.read(16)
        nonce = f.read(15)
        ciphertext = f.read()

    cipher = AES.new(aes_key, AES.MODE_OCB, nonce=nonce)
    try:
        message = cipher.decrypt_and_verify(ciphertext, tag)
    except ValueError:
        print("The message was modified!")
        sys.exit(1)

    print("Message:", message.decode())


x = encrypt()
print(x)
decrypt(x)
