import hashlib
import sys
import time
Maximum_Recursion_Limit = 2147483647
sys.setrecursionlimit(Maximum_Recursion_Limit)


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


try:
    print(f"{Maximum_Recursion_Limit = }")
    print("1  - MD5\n2  - SHA1\n3  - SHA224\n4  - SHA256\n5  - SHA384\n6  - SHA512\n7  - SHA3_224\n8  - SHA3_256\n\
9  - SHA3_384\n10 - SHA3_512\n11 - SHAKE_128\n12 - SHAKE_256\n13 - BLAKE2B\n14 - BLAKE2S")
    hash_type = int(input("hash_type >> "))
    hash_ = input("hash >> ")

    chars = str(input("Enter the set of All Possible Characters, separated by Space : "))
    k = int(input("Enter the Maximum Possible String Length (Time Consumption will be high if the entered number is greater one): "))
    set_ = chars.split()
    set_.append(" ")
    start = time.time()
    count = 1
    len_ = str(len(str(Maximum_Recursion_Limit)))
    while True:
        for i in range(1, k + 1):
            for j in range(len(set_)):
                strings = ['']
                for _ in range(i):
                    strings = [char + string for char in set_ for string in strings]
                for l in strings:
                    x = encode_word(l, hash_type)
                    if x == hash_:
                        print(f"Test case {count:0{len_}} - \033[92mPass\033[0m")
                        print(f"Time Consumed : {time.time()-start} seconds")
                        print(f"The Decrypted Form of \033[92m{hash_}\033[0m is \n\033[94m{l}\033[0m")
                        if True:
                            exit(0)
                    else:
                        print(f"Test case {count:0{len_}} - \033[91mFail\033[0m")
                    if count < Maximum_Recursion_Limit:
                        count += 1
                    else:
                        exit("Maximum Recursion Limit Reached ! Unable to find the correct string !")
except Exception as e:
    print(f"Error: {e}")
