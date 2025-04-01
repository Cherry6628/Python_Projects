try:
    min_length = int(input("Min Length >> "))
    max_length = int(input("Max Length >> "))
    characters = input("Characters >> ").split(" ")
    # a b c d e f g h   i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 0 1 2 3 4 5 6 7 8 9
except:
    exit()

for length in range(min_length, max_length + 1):
    for inp in __import__('itertools').product(characters, repeat=length):
        word = "".join(inp)
        with open(f"{min_length}-{max_length}_characters_({' '.join(characters)}).txt", 'a') as f:
            f.write(f"{word}\n")
