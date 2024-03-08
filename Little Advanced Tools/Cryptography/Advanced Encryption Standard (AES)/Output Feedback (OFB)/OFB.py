from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def encrypt(data, bits):
    key = get_random_bytes(bits//8)
    cipher = AES.new(key=key, mode=AES.MODE_OFB)
    ct_bytes = cipher.encrypt(data)
    return ct_bytes, key, cipher.iv


def decrypt(ct_bytes, key, iv):
    cipher = AES.new(key=key, mode=AES.MODE_OFB, iv=iv)
    pt = cipher.decrypt(ct_bytes)
    return pt


data_to_encrypt = b"OFB Mode"
bits_ = 256

ct_bytes_, key_, iv_ = encrypt(data_to_encrypt, bits_)
print(f"Encrypted Data : {ct_bytes_.hex()}\nKey : {key_.hex()}\nInitialization Vector (Nonce) : {iv_.hex()}")


plain_text = decrypt(ct_bytes_, key_, iv_)
print(f"\nDecrypted Plain Text : {plain_text}")
assert plain_text == data_to_encrypt
