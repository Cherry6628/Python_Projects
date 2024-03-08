def prime():
    try:
        inp = int(input("Enter the number here : "))
        for i in range(2, inp + 1):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i)
        print("\n")
        prime()
    except:
        prime()


prime()
