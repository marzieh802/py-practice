from random import randint


class Exercise():

    def rand_num(low, high, n):
        i = 1
        while (i <= n):
            yield randint(low, high)
            i += 1

    def iter_convert(name):
        return iter(name)

    def gen_comp(num):
        my_list = range(num)
        # generator comprehension
        gencomp = (item for item in my_list if item % 2 == 0)
        return gencomp
