def func():
    print("I am in module1 and my name is func")


def func1():
    print("I am func1")


def func3(num1):
    print("func3", num1)


if (__name__ == "__main__"):
    func()
    func1()
    func3(3)
    print("Top level in module1 of FirstPackage")
# else:
#     print("module1 of FirstPackage was imported")
