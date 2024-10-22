def hello(name):
    return f"hello,{name}"


def math_func(num1, num2, operation):
    print("this is math func")

    def plus_func():
        print("\tthis is plus func")
        return num1 + num2
    # plus_func()

    def minus_func():
        return num1 - num2

    if (operation == "+"):
        return plus_func  # return function
    elif (operation == "-"):
        return minus_func  # return function


def pregnant(baby):  # pass in function as parameter
    # print("inside pregnant function", type(baby))

    def print_baby_name():
        print(baby("jack"))

    return print_baby_name


def new_decorator(some_func):  # pass in function as parameter

    def inner_func():  # wrapping a function into another function
        print("before!")
        print(some_func())
        print("after!")

    return inner_func


if (__name__ == "__main__"):

    # def f1(p1="jack"):
    #     return f"I am {p1} in f1"

    # result = new_decorator(f1)
    # result()

    @new_decorator  # == code number of 46 and 47
    def f1(p1="jack"):
        return f"I am {p1} in f1"
    f1()
