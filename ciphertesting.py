from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import sys


def get_new_aes_key():
    aes_key = get_random_bytes(16)
    print(f"aes_key {aes_key}")
    return aes_key

get_new_aes_key()
