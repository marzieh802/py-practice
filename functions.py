# def say_hello(name):
#     '''
#     this is a multi line comment and
#     name is parameter
#     '''
#     print("hello",name)

# # person = "jack"
# # '''
# # a comment for p
# # '''


# # say_hello(person) #person is argument.


# # def add(num1,num2):
# #     result = num1 + num2
# #     return result
# # sum = add(88,2)
# # print(sum)

# def fizzbuzz_game(start,end):
#     result = ""
#     for inte in range(start,end):
#         if (inte % 3 == 0 and inte % 5 == 0):
#             result += "fizzBuzz"
#         elif inte %5 == 0:
#             result += "Buzz"
#         elif inte %3 == 0:
#             result += "Fizz"
#         else:
#             result += f"{inte}"
#         result += ", "

#     return result
# final = fizzbuzz_game(5,33)    #make dynomic the code
# print(final)

# # print(fizzbuzz_game(32,76))

# newstr = say_hello(final)
# print("newstr: ",newstr)
# print("newstr: ",type(newstr))
# hello my love
# def multiply(num1, num2=5, num3=4):
#     return num1*num2*num3


# res = multiply(3, 4)
# print(res)


def get_even_list(item):
    even_list = []
    for num in item:
        if (num % 2 == 0):
            even_list.append(num)
    return even_list


even = get_even_list([1, 2, 3, 4, 5, 6])
print(even)
