import random


def binary_evolution(num, mutation_probability):
    binary_string = str(bin(num))[2::]
    evolved_string = ""
    for bit in binary_string:
        if random.random() < mutation_probability:
            evolved_string += "1" if bit == "0" else "0"
        else:
            evolved_string += bit
    return int(evolved_string, 2)


starting_number = 1234234
evolved_num = binary_evolution(mutation_probability=0.1, num=starting_number)
print(f"Number at Starting of Evolution = {starting_number}")
print(F"Evolved Number                  = {evolved_num}\n")
variance = evolved_num-starting_number
print(F"Variance                        = {variance}")
if variance == 0:
    print("No Evolution Occurred")
else:
    print(F"Direction of Evolution          = %s" % ("Backward" if (evolved_num-starting_number) < 0 else "Forward"))
