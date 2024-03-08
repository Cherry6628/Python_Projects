# Bailey–Borwein–Plouffe (BBP) Formula
# π = summation of (4/(8k+1) - 2/(8k+4) - 1/(8k+5) - 1/(8k+6)) * ((1/16)**k) for k from 0 to infinity
from decimal import Decimal, getcontext


def pi_():
    try:
        accuracy = int(input("Enter the Accuracy for Calculating π : "))
        precision = getcontext().prec = int(input("Enter the Precision for Calculating π : "))
        pi = Decimal(0)
        for i in range(accuracy + 1):
            pi_h = Decimal(((4/((8*i)+1)) - (2/((8*i)+4)) - (1/((8*i)+5)) - (1/((8*i)+6))) * ((1/16)**i))
            pi += Decimal(pi_h)
        print("{:.{}f}".format(pi, precision))
        print("\n")
    except:
        print("\n")
    finally:
        pi_()


pi_()

