
def write_func():
    try:
        with open("test2.txt", mode='w') as content:  # this address is relative
            content.write(
                "write function in mode 'w' is for writing and creating")
            print(content.read())
            print("end of try")
    except:
        print("in write func there is an error")
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
