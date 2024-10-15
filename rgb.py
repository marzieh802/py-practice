def rgb():

    print("\033[38;2;255;51;51m")  # text color
    print("\033[48;2;128;223;255m")  # background color
    # this codes name is ansi escape code
    # "\033[38;2;......;m" and "\033[38;2;......;m" are constant
    # between rgb's numbers we have to put ';'


if (__name__ == "__main__"):
    rgb()
    print("this is a test")
    print("this is true color and")
