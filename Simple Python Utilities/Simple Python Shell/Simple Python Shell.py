while True:
    try:
        user_input = ""
        while True:
            line = input(">>> ")
            if line == "":
                break
            user_input += line + "\n"

        if user_input.strip().lower() == "help":
            print("1) Type \"exit\" or \"quit\" or \"kill\" or \"terminate\" to exit the terminal \
\n2) Type \"Restart\" to Restart the Terminal without clearing the screen.")
        elif user_input.strip() in ["exit", "quit", "kill", "terminate"]:
            exit("Exiting the Terminal")
        elif user_input.strip().lower() == "restart":
            print()
            exec(open(__file__).read())
        exec(user_input)

    except Exception as e:
        print("Error :", e)
