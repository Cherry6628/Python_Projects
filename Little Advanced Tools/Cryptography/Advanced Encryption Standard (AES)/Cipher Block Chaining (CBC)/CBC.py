from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def encrypt(data: bytes, bits: int):
    key = get_random_bytes(bits//16)
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    return ct_bytes, key, cipher.iv


def decrypt(ct_bytes, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct_bytes), AES.block_size)
    return pt


data_to_encrypt = b"CBC Mode"
bits_ = 256

ct_bytes_, key_, iv_ = encrypt(data_to_encrypt, bits_)
print(f"Encrypted Data : {ct_bytes_.hex()}\nKey : {key_.hex()}\nInitialization Vector (Nonce) : {iv_.hex()}")


plain_text = decrypt(ct_bytes_, key_, iv_)
print(f"\nDecrypted Plain Text : {plain_text}")
assert plain_text == data_to_encrypt
