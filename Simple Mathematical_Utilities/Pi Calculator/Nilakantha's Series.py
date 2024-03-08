# Nilakantha's Series
# π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - ...
def pi_():
    try:
        accuracy = int(input("Enter the Accuracy for Calculating π : "))
        precision = int(input("Enter the Precision for Calculating π : "))
        pi_h = 3
        for i in range(1, accuracy):
            a = ((-1) ** (i + 1)) * (4 / ((2 * i) * ((2 * i) + 1) * ((2 * i) + 2)))
            pi_h += a
        print("{:.{}f}".format(pi_h, precision))
        print("\n")
        pi_()
    except:
        print("\n")
        pi_()


pi_()
