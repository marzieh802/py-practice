from functions import summer_69
from FirstPackage.module1 import func
from FirstPackage.module1 import func3 as module_func  # .module1 = indirect run
from FirstPackage.SecondPackage import module1 as module2
# from FirstPackage import SecondPackage  error!!

if (__name__ == "__main__"):

    my_list = summer_69([1, 2, 3])
    print(my_list)

    module_func(3)
    module2.func()
    func()
