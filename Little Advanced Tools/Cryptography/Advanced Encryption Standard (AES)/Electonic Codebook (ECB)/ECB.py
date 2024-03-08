from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def encrypt(data, bits):
    key = get_random_bytes(bits//8)
    cipher = AES.new(key=key, mode=AES.MODE_ECB)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    return ct_bytes, key


def decrypt(ct_bytes, key):
    cipher = AES.new(key=key, mode=AES.MODE_ECB)
    pt = unpad(cipher.decrypt(ct_bytes), AES.block_size)
    return pt


data_to_encrypt = b"ECB Mode"
bits_ = 256

ct_bytes_, key_ = encrypt(data_to_encrypt, bits_)
print(f"Encrypted Data : {ct_bytes_.hex()}\nKey : {key_.hex()}")


plain_text = decrypt(ct_bytes_, key_)
print(f"\nDecrypted Plain Text : {plain_text}")
assert plain_text == data_to_encrypt