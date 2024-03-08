# Leibniz’s Formula
# π = 4(1 - 1/3 + 1/5 - 1/7 + 1/11 - ....)
def pi_():
    try:
        accuracy = int(input("Enter the Accuracy for Calculating π : "))
        precision = int(input("Enter the Precision for Calculating π : "))
        x = 0
        for i in range(1, accuracy + 1):
            pi_h = ((-1) ** (i + 1)) * (1 / ((2 * i) - 1))
            x += pi_h
        pi = x * 4
        print("{:.{}f}".format(pi, precision))
        print("\n")
        pi_()
    except:
        print("\n")
        pi_()


pi_()
