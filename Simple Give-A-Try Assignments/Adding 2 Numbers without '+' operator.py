try:
    x = int(input("n1 >> "))
    y = int(input("n2 >> "))
except:
    print(f"Values of n1 and n2 are changed due to invalid input !")
    x = 100
    y = 100
print(f"n1 = {x}\nn2 = {y}")
a = len(str(max(x, y)))

try:
    steps = int(input("\n1 - Show Steps\n0 - Not to Show Steps\n(If Anything entered except these, The Default Value will be used : 1)\n>> "))
except:
    steps = 1

print(f"Option : {steps}\n\n------------------------------------------------------------------------------------------")
print(f"x : {x:0{a}} | y : {y:0{a}} | temp : {'0':0{a}}")
while y != 0:
    temp = x & y
    x = x ^ y
    y = temp << 1
    if steps:
        print(f"x : {x:0{a}} | y : {y:0{a}} | temp : {temp:0{a}}")

print(f"\n\n\n{x}")
