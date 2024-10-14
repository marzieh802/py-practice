# isEven = 10 % 2

# if isEven:
#     print("10 is even")

def fact(num):

    res = 1
    i = 1
    while (i <= num):
        res *= i
        i += 1
    return res


if (__name__ == "__main__"):
    print(fact(10))
