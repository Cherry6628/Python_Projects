import hashlib


def encode_word(word, hash_type):
    if hash_type == 1:
        hash_object = hashlib.md5(word.encode())
    elif hash_type == 2:
        hash_object = hashlib.sha1(word.encode())
    elif hash_type == 3:
        hash_object = hashlib.sha224(word.encode())
    elif hash_type == 4:
        hash_object = hashlib.sha256(word.encode())
    elif hash_type == 5:
        hash_object = hashlib.sha384(word.encode())
    elif hash_type == 6:
        hash_object = hashlib.sha512(word.encode())
    elif hash_type == 7:
        hash_object = hashlib.sha3_224(word.encode())
    elif hash_type == 8:
        hash_object = hashlib.sha3_256(word.encode())
    elif hash_type == 9:
        hash_object = hashlib.sha3_384(word.encode())
    elif hash_type == 10:
        hash_object = hashlib.sha3_512(word.encode())
    elif hash_type == 11:
        hash_object = hashlib.shake_128(word.encode())
    elif hash_type == 12:
        hash_object = hashlib.shake_256(word.encode())
    elif hash_type == 13:
        hash_object = hashlib.blake2b(word.encode())
    elif hash_type == 14:
        hash_object = hashlib.blake2s(word.encode())
    else:
        return "Invalid hash type"

    return hash_object.hexdigest()


print("HASH ENCRYPTOR")
print("1  - MD5\n2  - SHA1\n3  - SHA224\n4  - SHA256\n5  - SHA384\n6  - SHA512\n7  - SHA3_224\n8  - SHA3_256\n\
9  - SHA3_384\n10 - SHA3_512\n11 - SHAKE_128\n12 - SHAKE_256\n13 - BLAKE2B\n14 - BLAKE2S")

try:
    print(encode_word(hash_type=int(input("Hash Type >> ")), word=input("Word >> ")))
except Exception as e:
    exit(f"Error : {e}")
