# Machin's Formula
# π = 16arctan(1/5) - 4arctan(1/239)
def arctan(x, terms):
    # arctan(x) = x - (x^3)/3 + (x^5)/5 - (x^7)/7 + ...
    result = 0
    for n in range(terms):
        arctan_x = ((-1)**n) * (x**(2*n + 1)) / (2*n + 1)
        result += arctan_x
    return result


def pi_():
    try:
        accuracy = int(input("Enter the Accuracy for Calculating π : "))
        precision = int(input("Enter the Precision for Calculating π : "))
        pi = (16 * arctan(1/5, accuracy)) - (4 * arctan(1/239, accuracy))
        print("{:.{}f}".format(pi, precision))
        print("\n")
        pi_()
    except:
        print("\n")
        pi_()


pi_()
