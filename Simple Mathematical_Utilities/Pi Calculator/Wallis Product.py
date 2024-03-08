# Wallis Product
# π/2 = ((4*2*2)/(1*3)) * ((4*4*4)/(3*5)) * ((4*6*6)/(5*7)) ...
def pi_():
    try:
        accuracy = int(input("Enter the Accuracy for Calculating π : "))
        precision = int(input("Enter the Precision for Calculating π : "))
        pi_h = 1
        for i in range(1, accuracy+1):
            pi_h *= ((4 * (i ** 2)) / ((4 * (i ** 2)) - 1))
        pi = pi_h * 2
        print("{:.{}f}".format(pi, precision))
        print("\n")
        pi_()
    except:
        print("\n")
        pi_()


pi_()
