import time


def fun1(param_to_func):  # this has responsibility for wrapping / decorator with wrapper
    print("inside fun1")

    def fun1_1(name2):  # this func is wrapper
        param_to_func("jack")  # this is the wrapped func by wrapper(fun1_1)
        print("inside func1_1", name2)
        return "return from fun1_1"
    return fun1_1


def fun2(name):  # we want to wrap this func
    print("inside fun2", name)


# print(fun1(fun2)())
dec = fun1(fun2)  # fun2-->param_to_func
print(dec("leo"))  # dec() is fun1_1


# *********************** the decorated one ***********************
print("\n*********************** the decorated one ***********************\n")


def fun1(param_to_func):
    print("inside fun1")

    def fun1_1(name2):
        param_to_func("jack")
        print("inside func1_1", name2)
        return "return from fun1_1, with print fun2"
    return fun1_1


@fun1
def fun2(name):
    print("inside fun2", name)


print(fun2("leo"))


# epoch(unix time)
print(int(time.time()*1000))
