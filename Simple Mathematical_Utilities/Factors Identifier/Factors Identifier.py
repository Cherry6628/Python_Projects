inp = int(input("Enter the Number here : "))
for i in range(1, inp+1):
    if inp % i == 0:
        print(i)
    else:
        continue
