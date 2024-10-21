# # def generate_num(num): # this func returns a list that contains 0 to num
# #     result = []
# #     for i in range(num):
# #         result.append(i)
# #     return result

# def generate_num(num):

#     for i in range(num):
#         yield i*2


# if (__name__ == "__main__"):
#     for x in generate_num(1000000):
#         print(x)

#     # print(list(generate_num(1000)))


def generate_num():
    yield 2 + 2
    # return 10 # will stop the generator from running
    yield 2 * 3
g = generate_num()
print(next(g))
print(next(g))


# list1 = list(range(0,10))
# print(list1)


# g1 = iter(range(0, 10))
# print(next(g1))
# print(next(g1))
# print(next(g1))


# g2 = iter("hello")
# try:
#     while True:
#         print(next(g2))
# except StopIteration:
#     print("generator has ended")

# list2 = [{"k":2},{"k2":7},"jack"]
# g3 = iter(list2) # iter func is for sth that is iterable and make that into generator
# print(next(g3))
# print(next(g3))
# print(next(g3))
