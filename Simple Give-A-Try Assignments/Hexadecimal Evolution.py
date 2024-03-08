import random


def hexadecimal_evolution(num, mutation_probability):
    hexadecimal_string = str(hex(num))[2::]
    evolved_string = ""
    for bit in hexadecimal_string:
        temporary_r = random.random()
        if temporary_r < mutation_probability:
            evolved_string += str(hex(int(int(bit, 16) + int(str(int((temporary_r*100)//1)), 16))//16))[2::]
        else:
            evolved_string += bit

    return int(evolved_string, 16)


starting_number = 1234234
evolved_num = hexadecimal_evolution(mutation_probability=0.9, num=starting_number)
print(f"Number at Starting of Evolution = {starting_number}")
print(F"Evolved Number                  = {evolved_num}\n")
variance = evolved_num-starting_number
print(F"Variance                        = {variance}")
if variance == 0:
    print("No Evolution Occurred")
else:
    print("Direction of Evolution          = %s" % ("Backward" if (evolved_num-starting_number) < 0 else "Forward"))

