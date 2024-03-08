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
        return word

    return hash_object.hexdigest()


default = "a b c d e f g h i j k l m n o p q r s t u v w x y z  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z \
0 1 2 3 4 5 6 7 8 9 . , / < > ? ; ' : \ ] [ { } | = - + _ ) ( * & ^ % $ # @ ! ~ ` ".split()
default.append(" ")

print(f"Default Characters List = {default}")


try:
    min_length = int(input("Min Length >> "))
    max_length = int(input("Max Length >> "))
    characters = input("Characters >> ").split().append(" ")
    if characters == "":
        characters = default
    print("1  - MD5\n2  - SHA1\n3  - SHA224\n4  - SHA256\n5  - SHA384\n6  - SHA512\n7  - SHA3_224\n8  - SHA3_256\n\
9  - SHA3_384\n10 - SHA3_512\n11 - SHAKE_128\n12 - SHAKE_256\n13 - BLAKE2B\n14 - BLAKE2S")
    hashtype = int(input("Hash Type  >>"))
    if 1 > hashtype > 14:
        raise Exception
except Exception:
    print("Invalid Input ! ")
    exit()

for length in range(min_length, max_length + 1):
    for inp in __import__('itertools').product(characters, repeat=length):
        word = "".join(inp)
        with open(f"{min_length}-{max_length}_characters_({' '.join(characters)}).txt", 'a') as f:
            f.write(f"{encode_word(word, hashtype)}\n")
