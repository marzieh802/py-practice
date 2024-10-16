from dec import hello, math_func, pregnant


if (__name__ == "__main__"):
    # print(hello("jack"))
    # var1 = hello
    # print(var1("var1"))

    # ope = math_func(1, 2, "+")
    # print(ope())

    # print(math_func(1, 2, "-")())  # call a anonymous function

    def baby_talk(name):
        return f"I am {name} baby"

    result = pregnant(baby_talk)
    result()
