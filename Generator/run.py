from homework import Exercise

if (__name__ == "__main__"):

    # for num in homework.rand_num(1,5,12):
    #   print(num)
    g = Exercise.rand_num(1, 3, 4)  # this will not run the function
    print(next(g))  # this will run the function until the yield keyword
    print(next(g))  # this will run function after the last yield until the next yield
    print("********************************")

    g1 = Exercise.iter_convert("I like nature")  # it returns generator
    for i in g1:
        print(i)

    print("********************************")
    g2 = Exercise.gen_comp(100)
    # for i in g2:
    #     print("inside g2", i)
    print("inside g2", next(g2))
    print("inside g2", next(g2))
    print("inside g2", next(g2))
    print("inside g2", next(g2))
