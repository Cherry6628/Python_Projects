class TextColor:
    @staticmethod
    def black():
        print("\033[30m", end="")

    @staticmethod
    def red():
        print("\033[31m", end="")

    @staticmethod
    def green():
        print("\033[32m", end="")

    @staticmethod
    def yellow():
        print("\033[33m", end="")

    @staticmethod
    def blue():
        print("\033[34m", end="")

    @staticmethod
    def magenta():
        print("\033[35m", end="")

    @staticmethod
    def cyan():
        print("\033[36m", end="")

    @staticmethod
    def white():
        print("\033[37m", end="")

    @staticmethod
    def bright_black():
        print("\033[90m", end="")

    @staticmethod
    def bright_red():
        print("\033[91m", end="")

    @staticmethod
    def bright_green():
        print("\033[92m", end="")

    @staticmethod
    def bright_yellow():
        print("\033[93m", end="")

    @staticmethod
    def bright_blue():
        print("\033[94m", end="")

    @staticmethod
    def bright_magenta():
        print("\033[95m", end="")

    @staticmethod
    def bright_cyan():
        print("\033[96m", end="")

    @staticmethod
    def bright_white():
        print("\033[97m", end="")


class BackgroundColor:
    @staticmethod
    def black():
        print("\033[40m", end="")

    @staticmethod
    def red():
        print("\033[41m", end="")

    @staticmethod
    def green():
        print("\033[42m", end="")

    @staticmethod
    def yellow():
        print("\033[43m", end="")

    @staticmethod
    def blue():
        print("\033[44m", end="")

    @staticmethod
    def magenta():
        print("\033[45m", end="")

    @staticmethod
    def cyan():
        print("\033[46m", end="")

    @staticmethod
    def white():
        print("\033[47m", end="")

    @staticmethod
    def bright_black():
        print("\033[100m", end="")

    @staticmethod
    def bright_red():
        print("\033[101m", end="")

    @staticmethod
    def bright_green():
        print("\033[102m", end="")

    @staticmethod
    def bright_yellow():
        print("\033[103m", end="")

    @staticmethod
    def bright_blue():
        print("\033[104m", end="")

    @staticmethod
    def bright_magenta():
        print("\033[105m", end="")

    @staticmethod
    def bright_cyan():
        print("\033[106m", end="")

    @staticmethod
    def bright_white():
        print("\033[107m", end="")


class TextStyle:
    @staticmethod
    def normal_style():
        print("\033[0m", end="")

    @staticmethod
    def bold():
        print("\033[1m", end="")

    @staticmethod
    def dim():
        print("\033[2m", end="")

    @staticmethod
    def italic():
        print("\033[3m", end="")

    @staticmethod
    def underline():
        print("\033[4m", end="")

    @staticmethod
    def blink():
        print("\033[5m", end="")

    @staticmethod
    def reverse():
        print("\033[7m", end="")

    @staticmethod
    def invisible():
        print("\033[8m", end="")

    @staticmethod
    def bold_off():
        print("\033[21m", end="")

    @staticmethod
    def normal_intensity():
        print("\033[22m", end="")

    @staticmethod
    def not_italic():
        print("\033[23m", end="")

    @staticmethod
    def underline_off():
        print("\033[24m", end="")

    @staticmethod
    def blink_off():
        print("\033[25m", end="")

    @staticmethod
    def inverse_off():
        print("\033[27m", end="")

    @staticmethod
    def reveal():
        print("\033[28m", end="")

    @staticmethod
    def not_crossed_out():
        print("\033[29m", end="")

    @staticmethod
    def framed():
        print("\033[51m", end="")

    @staticmethod
    def encircled():
        print("\033[52m", end="")

    @staticmethod
    def overlined():
        print("\033[53m", end="")

    @staticmethod
    def not_framed_or_encircled():
        print("\033[54m", end="")

    @staticmethod
    def not_overlined():
        print("\033[55m", end="")


def Reset():
    print("\033[0m", end="")
