def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact


def euler_number(acc=0, pre=0):
    e = 0
    for i in range(acc):
        e += 1/factorial(i)
    print("{:.{}f}".format(e, pre))
    print(f"{l}{l}")


l = "_______________________________________________________________________________________________________________"
while True:
    try:
        euler_number(int(input("Accuracy : ")), int(input("Precision : ")))
    except Exception as i:
        print(f"Error : {i} \n{l}{l}")
