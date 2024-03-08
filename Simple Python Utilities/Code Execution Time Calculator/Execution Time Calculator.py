import timeit
import re
code = ""
try:
    counts = int(input("How many times your code have to run ?\n(This is used only for calculating \
the average time for each Execution)\n"))
    print("Your Python Code Here ! 👇👇🏻👇🏼👇🏽👇🏾")
    while True:
        inp = input(">> ")
        if inp != "":
            code += inp + "\n"
        else:
            break
    if "exit" in code:
        exit("You are trying to access the vulnerable part of the code... And that's not fair")
    time_ = timeit.timeit(stmt=f"""{code}""", number=counts)
    time = time_/counts
    print(f"\n\nTotal Number of Execution(s) = {counts}\nAverage time for Executing   = Total time taken/\
Number of Executions = {time_}/{counts} = {time} seconds 👀")

except Exception as e:
    print("Error :", e)
