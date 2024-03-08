# Function to generate a range of floating-point numbers with specified start, end, and interval
def f_range(starting_num: float = 0.0, ending_num: float = 1.0, interval_float: float = 1.0) -> iter:
    i = starting_num
    if interval_float >= 0:
        while i <= ending_num:
            yield i
            i += interval_float
    else:
        while i >= ending_num:
            yield i
            i += interval_float


# def logarithm(number: float = 10.0, base: float = 10.0) -> float:  # Brute forcing way of finding Logarithm
#     temp = 0
#     for i in f_range(0.0, float(number), 0.0001):
#         if number > (base ** i) > (base ** temp):
#             temp = i
#     return temp


# Function to calculate logarithm with a specified base
def logarithm(number: float = 10.0, base: float = 10.0) -> float:
    if (base % 10 == 0) and (number % 10 == 0) and (float(str(base)[1::]) == 0.0) and (float(str(number)[1::]) == 0.0):
        # If base and number are multiples of 10, calculate logarithm using digit lengths
        temp_base = len(str(base)[1::])
        temp_num = len(str(number)[1::])
        current_len = temp_num / temp_base
        return current_len
    else:
        # If not, use binary search to find the logarithm
        low = 0
        high = number
        mid = 0
        max_iterations = 1000000

        for _ in range(max_iterations):
            mid = (low + high) / 2
            if base < number ** (1/mid):
                low = mid
            else:
                high = mid
            if high - low < 0.00000001:
                break

        return mid


# Function to calculate antilogarithm with a specified base
def antilogarithm(number: float = 1.0, base: float = 10.0) -> float:
    return base ** number


# Function to handle the first user input
def select_operation() -> int:
    print("1 - Logarithm\n2 - Antilogarithm\nOther Response - Exit")
    inp1 = input(">> ").replace(" ", "")
    if inp1 == '1':
        return select_logarithm_type()
    elif inp1 == '2':
        return select_antilogarithm_type()
    else:
        exit()


# Function to handle the second user input for logarithm options
def select_logarithm_type():
    print("1 - Logarithm            - log()\n2 - Natural Logarithm    - ln()\nOther Response - Go Back")
    inp2 = input(">> ").replace(" ", "")
    if inp2 == '1':
        return 1
    elif inp2 == '2':
        return 2
    else:
        select_operation()


# Function to handle the second user input for antilogarithm options
def select_antilogarithm_type():
    print("1 - Anti-Logarithm       - log^-1()\n2 - Exponential Function - ln^-1()\nOther Response - Go Back")
    inp3 = input(">> ").replace(" ", "")
    if inp3 == '1':
        return 3
    elif inp3 == '2':
        return 4
    else:
        select_operation()


# Main loop to interact with the user and perform calculations
def main_loop():
    e = 2.7182818284590452353602874713527
    x = select_operation()
    while True:
        try:
            if x == 1:
                b = float(input("Base   >> "))
                n = float(input("Number >> "))
                y = logarithm(number=n, base=b)
            elif x == 2:
                n = float(input("Number >> "))
                y = logarithm(number=n, base=e)
            elif x == 3:
                b = float(input("Base   >> "))
                n = float(input("Number >> "))
                y = antilogarithm(number=n, base=b)
            elif x == 4:
                n = float(input("Number >> "))
                y = antilogarithm(number=n, base=e)
            print("Approximate Value :", round(y, 5))
            print("\n\n")
        except ValueError:
            print("Value Error")
            # Handle input errors by calling appropriate input functions
            if x in [1, 2]:
                select_logarithm_type()
            elif x in [3, 4]:
                select_antilogarithm_type()
            else:
                select_operation()
        except Exception as e:
            # Handle other exceptions and exit the application
            exit(f"Error : {e}\nSorry for the Inconvenience ! There is a Bug in the Application...\nExiting \
the Application...")


# Run the main loop
main_loop()
