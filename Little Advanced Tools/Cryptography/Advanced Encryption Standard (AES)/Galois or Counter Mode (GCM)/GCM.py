from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def encrypt(data, bits, header):
    key = get_random_bytes(bits // 8)
    cipher = AES.new(key=key, mode=AES.MODE_GCM)
    cipher.update(header)
    ct_bytes, tag = cipher.encrypt_and_digest(data)
    return ct_bytes, key, cipher.nonce, tag, header


def decrypt(ct_bytes, key, iv, tag, header):
    cipher = AES.new(key=key, mode=AES.MODE_GCM, nonce=iv)
    cipher.update(header)
    pt = cipher.decrypt_and_verify(ct_bytes, tag)
    return pt


data_to_encrypt = b"GCM Mode"
header_message = b'This is GCM Mode'
bits_ = 256

ct_bytes_, key_, iv_, tag_, header_ = encrypt(data_to_encrypt, bits_, header_message)
print(f"Encrypted Data : {ct_bytes_.hex()}\nKey : {key_.hex()}\nInitialization Vector (Nonce) : {iv_.hex()}\nTag : {tag_.hex()}")

plain_text = decrypt(ct_bytes_, key_, iv_, tag_, header_)
print(f"\nDecrypted Plain Text : {plain_text}")
assert plain_text == data_to_encrypt
