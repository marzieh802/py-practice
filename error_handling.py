
def write_func():
    try:
        with open("test2.txt", mode='w') as content:  # this address is relative
            content.write(
                "write function in mode 'w' is for writing and creating")
            print(content.read())
            print("end of try")
    except TypeError:
        print("in write func there is TypeError")
    except IOError:
        print("in write func there is IOError")
    except:
        print("in write func there is for all error")
    finally:
        print("this is finally")  # this is always works!


def add(num1, num2):
    return num1+num2


def get_num():
    while True:
        try:
            res = int(input("write a number"))
            print("thank you for ", res)
            break
        except:
            print("you entered a wrong input")

# homework


def problem1():
    try:

        for i in ['a', 'b', 'c']:
            print(i**2)  # exception thrown by this line
    except TypeError:
        print("this is a TypeError from problem1 function")


def problem2():
    try:

        x = 5
        y = 0
        z = x/y
    except ZeroDivisionError:
        print("this is a ZeroDivisionError from problem2 function")
    finally:
        print("All Done from problem2 function(finally)")


problem2()


def ask():
    '''this function has an error that depends on input'''
    while True:
        # you have to use the functions' output
        try:
            num = int(input("Input an integer:"))
            print("Thank you, your number squared is :", num**2)
            break
        except ValueError:
            print("An error occurred! Please try again!")
