li = []
threshold = 60000
weight = 0


def print_All_K_Length(set__, length):
    for i in range(1, k+1):
        for j in range(len(set__)):
            for string in generate_strings(set__, i):
                if string not in li:
                    with open(str(length) + " Character(s) (" + chars + ").txt", 'a') as f:
                        f.write(f"{string}\n")
                    li.append(string)
                    global weight
                    weight += 1
                    if weight == threshold:
                        li.clear()


def generate_strings(set__, n):
    if n == 0:
        return ['']
    strings = []
    for char in set__:
        for string in generate_strings(set__, n-1):
            strings.append(char + string)
    return strings


try:
    chars = str(input("_________________________\nPossible Characters (separated by Space) >> "))
    k = int(input("_____________________________________\nMaximum String Length >> "))
except Exception as e:
    exit(f"Error : {e}")

word = chars
set_ = word.split()
set_.append(" ")
print_All_K_Length(set_, k)
