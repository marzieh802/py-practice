from error_handling import write_func
from error_handling import add as add_nums
from error_handling import get_num

if (__name__ == "__main__"):
    try:
        get_num()
        write_func()  # it has try so in its layer the error get handled and there is no need to write inside another 'try'
        print(add_nums(2, '4'))
    except:
        print("this except is for add_nums")  # error bubbling

    print("program is exiting")
